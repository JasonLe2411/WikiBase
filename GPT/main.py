from pathlib import Path
import os
import yaml

import concurrent.futures 
import asyncio
import time

from llama_index import SimpleDirectoryReader, GPTListIndex, LLMPredictor
from langchain import OpenAI


def init_openai_keys() -> None:
    with open('secrets.yaml', 'r') as f:
        secrets = yaml.safe_load(f)
        os.environ['OPENAI_API_KEY'] = secrets['OPENAI_API_KEY']


def init_env() -> dict:
    env = {}
    with open('env.yaml', 'r') as f:
        env_yaml = yaml.safe_load(f)
        env['max_topics'] = env_yaml['max_topics']
        env['max_sections'] = env_yaml['max_sections']
        env['data_path'] = env_yaml['data_path']
    return env


def init_llm() -> LLMPredictor:
    temperature = 0
    model_name = 'text-davinci-003'
    max_tokens = 768 
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=temperature, model_name=model_name, max_tokens=max_tokens))
    return llm_predictor


def init_index(datapath: Path) -> GPTListIndex:
    init_openai_keys()
    key = datapath.name.rstrip('/')
    indexpath = Path('store').joinpath(f'{key}.json')

    index = None

    llm = init_llm()

    if indexpath.exists():
        print('Loading existing vector index')
        index = GPTListIndex.load_from_disk(indexpath, llm_predictor=llm)
    else:
        print('Initializing new vector index...')
        documents = SimpleDirectoryReader(datapath).load_data()
        index = GPTListIndex(documents, llm_predictor=llm)
        index.save_to_disk(indexpath)

    return index


class WikiGen:
    def __init__(self):
        env = init_env()

        self.max_topics = env['max_topics']
        self.max_sections = env['max_sections']

        self.data_path = Path(env['data_path'])
        self.key = self.data_path.name.rstrip('/')

        self.index = init_index(self.data_path)

        self.executor = concurrent.futures.ThreadPoolExecutor()

    def generate_wiki(self):
        topic_pool = self.index.query(
                '''Retrieve all topics from the document if it is "sufficiently talked about". Consider
                "sufficiently talked about" as a topic which has been talked about for 300 words or more. Return this
                as a comma-separated list.'''
        ).response.split(',')
        topics = topic_pool[:self.max_topics] if len(topic_pool) >= self.max_topics else topic_pool

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for topic in topics:
                futures.append(executor.submit(self._generate_sections, topic))
                time.sleep(0.5)  # Delay to avoid OpenAI anti-DDOS

            for f in concurrent.futures.as_completed(futures):
                result = f.result()

    def _generate_sections(self, raw_topic: str) -> Path:
        topic = raw_topic.strip().capitalize()
        page = f'# {topic}\n'

        section_query = f'Generate subtopics about the topic "{topic}" as a comma-separated list.'
        section_pool = self.index.query(section_query).response.split(',')
        sections = section_pool[:self.max_sections] if len(section_pool) >= self.max_sections else section_pool

        content_query = f'Fill in the Markdown template below:\n\n\n## Introduction\n<introduction about {topic}>\n'

        for section in sections:
            section = section.strip()
            form = f'## {section}\n<summary about {section}>\n'
            content_query += form

        print(content_query)
        content = self.index.query(content_query).response

        page += content 
        print(page)

        # save output to .md
        formatted_topic = topic.replace(' ', '_')
        output_path = Path('summaries').joinpath(f'{self.key}', f'{formatted_topic}.md')
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # filter out invalid characters and write to .md
        output_path.write_text(''.join(c for c in page if ord(c) < 128)) 

        return output_path
        

if __name__ == '__main__':
    wiki = WikiGen()
    wiki.generate_wiki()

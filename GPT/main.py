import argparse
from pathlib import Path
import os
import yaml

from llama_index import SimpleDirectoryReader, GPTListIndex, LLMPredictor
from langchain import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='doc-query')
    parser.add_argument('datapath', type=Path)
    return parser.parse_args()


def init_openai_keys() -> None:
    with open('secrets.yaml', 'r') as f:
        secrets = yaml.safe_load(f)
        os.environ['OPENAI_API_KEY'] = secrets['OPENAI_API_KEY']


def init_env() -> dict[str, int]:
    env = {}
    with open('env.yaml', 'r') as f:
        env_yaml = yaml.safe_load(f)
        env['max_topics'] = env_yaml['max_topics']
        env['max_sections'] = env_yaml['max_sections']
    return env


def init_llm() -> LLMPredictor:
    temperature = 0
    model_name = 'text-davinci-003'
    max_tokens = 512 
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



def wiki_summary() -> str:
    args = parse_args()
    index = init_index(args.datapath)
    key = args.datapath.name.rstrip('/')

    env = init_env()
    max_topics = env['max_topics']
    max_sections = env['max_sections']

#   all_topics = index.query(
#           '''Retrieve all topics from the document if it is "sufficiently talked about". Consider
#           "sufficiently talked about" as a topic which has been talked about for 300 words or more. Return this
#           as a comma-separated list.'''
#   ).response.split(',')

    topic_pool = 'Multi-Head Attention, Scaled Dot-Product Attention, Self-Attention'.split(',')
    topics = topic_pool[:max_topics] if len(topic_pool) >= max_topics else topic_pool

    print('Generating topics for:', topics)
    for topic in topics:
        topic = topic.strip()
        page = f'# {topic}\n'

        section_query = f'''Generate subtopics about the topic "{topic}" as a comma-separated list.'''
        section_pool = index.query(section_query).response.split(',')
        sections = section_pool[:max_sections] if len(topic_pool) >= max_sections else section_pool

        content_query = f'''
Fill in the template below:\n
## Introduction\n
<introduction about {topic}>\n'''

        for section in sections:
            section = section.strip()
            form = f'''
## {section}\n
<summary about {section}>\n'''
            content_query += form

        print(content_query)
        content = index.query(content_query).response
        page += content 

        print(page)

        formatted_topic = topic.strip().replace(' ', '_')
        output_path = Path('summaries').joinpath(f'{key}', f'{formatted_topic}.md')

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(''.join(c for c in page if ord(c) < 128)) # filter out invalid characters

        print(f'Created .md for {topic}')


if __name__ == '__main__':
    wiki_summary()

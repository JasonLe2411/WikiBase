import argparse
from pathlib import Path
import os
import yaml

from llama_index import SimpleDirectoryReader, GPTListIndex 


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='doc-query')
    parser.add_argument('datapath', type=Path)
    return parser.parse_args()


def init_openai_keys() -> None:
    with open('secrets.yaml', 'r') as f:
        secrets = yaml.safe_load(f)
        os.environ['OPENAI_API_KEY'] = secrets['OPENAI_API_KEY']


def init_index(datapath: Path) -> GPTListIndex:
    init_openai_keys()
    key = datapath.name.rstrip('/')
    indexpath = Path('store').joinpath(f'{key}.json')

    index = None

    if indexpath.exists():
        print('Loading existing vector index')
        index = GPTListIndex.load_from_disk(indexpath)
    else:
        print('Initializing new vector index...')
        documents = SimpleDirectoryReader(datapath).load_data()
        index = GPTListIndex(documents)
        index.save_to_disk(indexpath)

    return index


def wiki_summary() -> str:
    args = parse_args()
    index = init_index(args.datapath)
    key = args.datapath.name.rstrip('/')

    all_topics = index.query(
            '''Retrieve all topics from the document if it is "sufficiently talked about". Consider
            "sufficiently talked about" as a topic which has been talked about for 300 words or more. Return this
            as a comma-separated list.'''
    )
    print('Generating topics for:', all_topics)

    for topic in all_topics.response.split(','):
        page = f'# {topic}\n'

        query_str = f'''
        Generate a summary for each entry in a table of contents of the topic '{topic}' in this text in the form:
        ## <entry> \n
        <summary> \n
        \n
        Make sure to include who spoke in the summaries.
        '''

        summary = index.query(query_str)
        page += summary.response
        
        formatted_topic = topic.strip().replace(' ', '_')
        output_path = Path('summaries').joinpath(f'{key}', f'{formatted_topic}.md')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(page.join(c for c in s if ord(c) < 128)) # filter out invalid characters

        print(f'Created .md for {topic}')



if __name__ == '__main__':
    wiki_summary()

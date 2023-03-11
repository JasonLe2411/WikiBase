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


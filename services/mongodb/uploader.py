# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------
# MongoFactory().insert_sample_collection()

import argparse
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from services.mongodb.utils import MongoFactory
from services.mongodb.configurations import LOGGER, NAS


def get_dataset(name: str, type: str):
    """read particular dataset

    Returns:
         rows List[Dict]: list of dicts where each dict corresponds to single row of dataset
    """
    LOGGER.info(f'Reading {name}/{type}.csv data')

    source = Path(NAS, name)
    data = pd.read_csv(source / f'{type}.csv').set_index('id').T.to_dict()
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MongoDB interface to upload dataset", add_help=True)
    parser.add_argument('-d', '--dataset', action="store", help="source dataset name",
                        choices=['CICIDS', 'NET', 'TRANSFORMED_CICIDS', 'TRANSFORMED_NET'], required=True)

    parser.add_argument('-t', '--type', action="store", help="type of dataset",
                        choices=['train', 'test'], required=True)

    args = parser.parse_args()

    MongoFactory().get_db()
    status = MongoFactory().server_status()
    configurations = MongoFactory().get_configuration()
    LOGGER.info(f'Database status: {status}')
    LOGGER.info(f'Database configurations: {configurations}')

    data = get_dataset(args.dataset, args.type)

    for index, id, in tqdm(enumerate(data)):
        MongoFactory().insert_row(_id=index, row=data[id], type=args.type, collection_name=args.dataset, verbose=True)




# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import argparse
from pathlib import Path

import pandas as pd

from transformer.configurations import LOGGER, DROP_COLUMNS_CICIDS, DROP_COLUMNS_NET


class Transformer:
    def __init__(self, dataset):
        self.dataset_name = dataset
        self.source_path = Path(Path.cwd(), 'NAS', dataset)
        self.destination_path = Path(Path.cwd(), 'NAS', f'TRANSFORMED_{dataset}')

        LOGGER.info(f'Created destination folder {self.destination_path}')
        self.destination_path.mkdir(parents=True, exist_ok=True)

    def _validate_dataset(self):
        """return related to particular dataset paths to transform
        """

        train_path = self.source_path / 'train.csv'
        test_path = self.source_path / 'test.csv'

        LOGGER.debug(f"--> Train file path: {train_path}")
        LOGGER.debug(f"--> Test file path: {test_path}")

        return train_path, test_path

    def _filter_dataset(self, path):
        df = pd.read_csv(path)
        if self.dataset_name == 'CICIDS':
            df = df.drop(columns=DROP_COLUMNS_CICIDS, axis=1)
            return df
        else:
            df = df.drop(columns=DROP_COLUMNS_NET, axis=1)
            return df

    def _save_train_csv(self, dataframe: pd.DataFrame):
        destination = self.destination_path / 'train.csv'
        dataframe.to_csv(destination, index=False)
        return True

    def _save_test_csv(self, dataframe: pd.DataFrame):
        destination = self.destination_path / 'test.csv'
        dataframe.to_csv(destination, index=False)
        return True

    def run(self):
        LOGGER.info(f"Transform {self.dataset_name} dataset")
        train_path, test_path = self._validate_dataset()

        train_df = self._filter_dataset(path=train_path)
        test_df = self._filter_dataset(path=test_path)
        LOGGER.info(f"Filtered TRAIN & TEST SET OF {self.dataset_name} dataset")

        self._save_train_csv(dataframe=train_df)
        self._save_test_csv(dataframe=test_df)
        LOGGER.info(f"Saved TRAIN & TEST SET under {self.destination_path}")

        LOGGER.info(f"Successfully transformed {self.dataset_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inplace Data Extractor", add_help=True)
    parser.add_argument('-d', '--dataset', action="store", help="source dataset name",
                        choices=['CICIDS', 'NET'], required=True)
    
    args = parser.parse_args()

    print(Transformer(dataset=args.dataset).run())





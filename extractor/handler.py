# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import os
import gzip
import json
import argparse

from tqdm import tqdm
from pathlib import Path

import pandas as pd

from extractor.configurations import LOGGER, MAPPING_NAMES


class Extractor:
    def __init__(self, dataset):
        self.dataset_name = dataset
        self.source_path = Path(Path.cwd(), 'source_data', dataset)
        self.destination_path = Path(Path.cwd(), 'NAS', dataset)

    def _validate_dataset(self):
        """return related to particular dataset paths to extract
        """

        labels_folder_name = MAPPING_NAMES.get("labels")
        train_folder_name = MAPPING_NAMES.get("train")
        test_folder_name = MAPPING_NAMES.get("test")

        label_path = self.source_path / labels_folder_name
        train_path = self.source_path / train_folder_name
        test_path = self.source_path / test_folder_name

        _label_files = [file for file in os.listdir(label_path) if file.endswith('.json.gz')]
        _train_files = [file for file in os.listdir(train_path) if file.endswith('.json.gz')]
        _test_files = [file for file in os.listdir(test_path) if file.endswith('.json.gz')]

        LOGGER.info(f"--> Train file name: {_train_files}")
        LOGGER.info(f"--> Test file name: {_test_files}")
        LOGGER.info(f"--> Labels files names: {_label_files}")

        return _train_files, _test_files, _label_files

    @staticmethod
    def read_json_gz(path):
        with gzip.open(path, "rb") as jj:
            rows = []
            corrupted_line = []

            _bar = tqdm(total=500000, initial=1)

            i = 0
            while True:
                i += 1
                try:
                    flow = jj.readline() # .decode("utf-8")
                    _bar.update(1)
                    if not flow:
                        break
                    row = json.loads(flow)
                    rows.append(row)
                except:
                    LOGGER.warning(f'Found beat line')
                    corrupted_line.append(i)

        _bar.close()
        LOGGER.info(f'----> Extracted rows --> {len(rows)}')
        LOGGER.warning(f'----> Corrupted row --> {len(corrupted_line)}')
        return rows

    def _get_train_data(self, files):
        """
        Notes:
            we expect just one train file for each dataset
        """

        train_folder_name = MAPPING_NAMES.get("train")
        file_path = self.source_path / train_folder_name / files[0]

        LOGGER.info(f"----> Retrieving train data: {file_path}")
        data = self.read_json_gz(file_path)
        return data

    def _get_test_data(self, files):
        """
        Notes:
            we expect just one train file for each dataset
        """

        test_folder_name = MAPPING_NAMES.get("test")
        file_path = self.source_path / test_folder_name / files[0]

        LOGGER.info(f"Retrieving test data: {file_path}")
        data = self.read_json_gz(file_path)
        return data

    def _get_labels(self, files):
        binary_labels = []
        multi_labels = []
        for index, file in enumerate(files):
            label_folder_name = MAPPING_NAMES.get("labels")
            file_path = self.source_path / label_folder_name / file
            LOGGER.info(f"----> Retrieving labels {index+1}/{len(files)}: {file_path}")

            with gzip.open(file_path, "rb") as jj:
                data = json.loads(jj.read())

            values = set(data.values())
            if len(values) == 2:
                LOGGER.info(f'------> Retrieved BINARY labels with unique classes={len(values)}')
                binary_labels.append(data)
            else:
                LOGGER.info(f'------> Retrieved MULTI labels with unique classes={len(values)}')
                multi_labels.append(data)

        return binary_labels, multi_labels

    def _save_train(self, data, binary, multi):
        LOGGER.info(f'------> Saving train data')
        df = pd.DataFrame(data)
        binary_series = pd.Series(binary[0])
        multi_series = pd.Series(multi[0])

        binary_df = pd.DataFrame({'id': binary_series.index.astype('int'), 'binary_class': binary_series.values})
        multi_df = pd.DataFrame({'id': multi_series.index.astype('int'), 'multi_class': multi_series.values})

        df = df.merge(binary_df, how='inner', on='id')
        df = df.merge(multi_df, how='inner', on='id')

        LOGGER.info(f'------> Merged train data with labels')

        self.destination_path.mkdir(parents=True, exist_ok=True)
        LOGGER.info(f'------> Created destination folder: {self.destination_path}')

        destination = self.destination_path / 'train.csv'
        df.to_csv(destination, index=False)
        LOGGER.info(f'------> Write train.csv to destination')
        return True

    def _save_test(self, data):
        LOGGER.info(f'------> Saving test data')
        df = pd.DataFrame(data)

        destination = self.destination_path / 'test.csv'
        df.to_csv(destination, index=False)
        LOGGER.info(f'------> Write test.csv to destination')
        return True

    def run(self):
        LOGGER.info(f"Extracting {self.dataset_name} dataset")
        train_files, test_files, label_files = self._validate_dataset()

        binary_labels, multi_labels = self._get_labels(files=label_files)  # List[Dict] List[Dict]
        train_data = self._get_train_data(files=train_files)
        self._save_train(data=train_data, binary=binary_labels, multi=multi_labels)

        test_data = self._get_test_data(files=test_files)  # List[Dict]
        self._save_test(data=test_data)

        LOGGER.info(f"Successfully extracted {self.dataset_name} dataset")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inplace Data Extractor", add_help=True)
    parser.add_argument('-d', '--dataset', action="store", help="source dataset name",
                        choices=['CICIDS', 'NET'], required=True)

    args = parser.parse_args()

    Extractor(dataset=args.dataset).run()





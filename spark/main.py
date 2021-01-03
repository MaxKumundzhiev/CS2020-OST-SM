# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------


import json
import pandas as pd

from pyspark import SparkContext

from spark.configurations import LOGGER, TRAIN_CICI, TRAIN_NET, TRAIN_VPN
from spark.utils.factory import Factory, Transformer, Visualiser


"""
1. Read/Write datasets from DBs [Class Reader]
    - mute it and read/write locally
2. Transform datasets [Class Transformer]
3. Visualise transformations/feature_importance [Class Visualiser]       
"""

import os
import argparse
from pathlib import Path

import findspark

from pyspark.sql import SparkSession
from spark.configurations import LOGGER


class Reader(Factory):
    @staticmethod
    def read_data(target_path):
        files = os.listdir(target_path)
        train_file = [file for file in files if file.endswith('.csv')][0]  # PATH_TO_RESULT_FOLDER/X_train.csv
        train_file = Path(target_path, train_file)

        assert train_file.exists(), 'FileNotFound: there is no such file or directory'

        # entry point of SparkSession
        findspark.init()
        spark = SparkSession.builder.appName(__name__).getOrCreate()
        df = spark.read.option('header', True, delimiter=';').csv(train_file)

        return df


def main():
    parser = argparse.ArgumentParser(description="Spark entry point", add_help=True)

    parser.add_argument('-d', '--dataset',
                        required=True,
                        action="store",
                        help="target dataset path"
                        )

    parser.add_argument('-t', '--type',
                        required=True,
                        action="store",
                        choices=['a', 'b', 'c'],
                        help="selection algorithm type"
                        )
    args = parser.parse_args()

    LOGGER.info(f'Reading dataset: {args.dataset}')
    data = Reader().read_data(args.dataset)
    return data


if __name__ == "__main__":
    print(main())











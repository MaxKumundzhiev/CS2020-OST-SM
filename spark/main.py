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

import pyspark
import argparse


class Reader(Factory):
    def read_data(self):
        pass


def main():
    parser = argparse.ArgumentParser(description="Spark entry point", add_help=True)
    parser.add_argument('-d', '--dataset', action="store", help="target dataset path")


if __name__ == "__main__":
    pass
    pyspark.read.json("<PATH_to_JSON_File>", multiLine = "true")










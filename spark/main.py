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


class Reader(Factory):
    def read_data(self):
        pass


with open(TRAIN_VPN, 'rb') as f:
    data = f.readlines()

from pyspark.sql.functions import *
import pyspark


rawDF = pyspark.read.json("<PATH_to_JSON_File>", multiLine = "true")










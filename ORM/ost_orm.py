from mongoengine import *
import datetime, os
import configparser
from bson.objectid import ObjectId


config = configparser.ConfigParser()
dir_path = os.path.dirname(os.path.realpath(__file__))
config.read(dir_path+'/../config.ini')

# Mongo
mongodb = config['db']['mongodb']
mongoport = int(config['db']['mongoport'])
cve_collection = config['db']['cve_collection']
mongo_database = config['db']['mongodatabase']

connect(
    db=mongo_database,
    host=mongodb,
    port=mongoport
)

#Creating a collection and document schema

class cisco(Document):
    _id = ObjectIdField(default=ObjectId)
    rev_pld_var = FloatField()
    src_port = IntField()
    pld_distinct = IntField()
    rev_hdr_ccnt = ListField()
    bytes_out = IntField()
    hdr_mean = FloatField()
    rev_intervals_ccnt = ListField()
    time_length = FloatField()
    num_pkts_out = IntField()
    pld_ccnt = ListField()
    pld_mean = FloatField()
    rev_pld_distinct = IntField()
    num_pkts_in = IntField()
    hdr_distinct = IntField()
    rev_hdr_distinct = IntField()
    hdr_bin_40 = IntField()
    pr = IntField()
    pld_max = IntField()
    hdr_ccnt = ListField()
    rev_pld_max = IntField()
    ack_psh_rst_syn_fin_cnt = ListField()
    pld_bin_inf = IntField()
    rev_pld_mean = FloatField()
    pld_median = IntField()
    dst_port = IntField()
    sa = StringField()
    rev_pld_bin_128 = IntField()
    da = StringField()
    intervals_ccnt = ListField()
    rev_ack_psh_rst_syn_fin_cnt = ListField()
    rev_hdr_bin_40 = IntField()
    rev_pld_ccnt = ListField()
    bytes_in = IntField()
    id = StringField(required=True, unique=True)

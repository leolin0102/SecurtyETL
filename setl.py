__author__ = 'lin'
import argparse
import daemon
import time

from connector.datasource import *
from mongo.mongo_connector import *

def do_main_program():
    datasource = MongoDatasource('crashes', 'OrionDB', '172.29.0.85')
    print datasource.row_count()
    data_set = datasource.row_data_set()
    time.sleep(10)

if __name__ == '__main__':
    # with daemon.DaemonContext():
    #     do_main_program()
    do_main_program()

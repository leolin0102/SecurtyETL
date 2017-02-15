__author__ = 'lin'
import argparse
import daemon
import time
import yaml
from connector.datasource import *
from robbot.robbot import *
from dwc.wit_data_warehouse_sync_client import WitDataWarehouseClient

from mongo.mongo_connector import *

def do_main_program():
    wit_client = WitDataWarehouseClient()
    datasource = MongoDatasource('crashes', 'OrionDB', '172.29.0.85')
    print datasource.row_count()

def start_robbot():
    robbot = Robbot()
    robbot.run()


if __name__ == '__main__':
    # with daemon.DaemonContext():
    #     do_main_program()

    # do_main_program()

    start_robbot()

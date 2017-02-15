__author__ = 'lin'

from pymongo import MongoClient


MONGO_SYNC_STATE = 'mongo_sync_state'
mongo_client = None

react_map = None

def connect_to_mongo(state, discover, context):
    global mongo_client
    mongo_client = MongoClient()
    print mongo_client

def discover_data_struct(state, discover, context):
    for db in mongo_client.database_names():
        print 'database: ', db
        print mongo_client[db].collection_names(False)


def finished(state, discover, context):
    return True

def register_mongo_reace(react_stack):
    react_stack.register_react('init', connect_to_mongo)



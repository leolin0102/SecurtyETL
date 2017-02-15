__author__ = 'lin'

from pymongo import MongoClient
from robbot.behavior.behavior import RobbotState
from robbot.env.task import Task, TaskState

MONGO_SYNC_STATE = 'mongo_sync_state'
mongo_client = None

react_map = None



def get_react_with_context(context):
    if MONGO_SYNC_STATE not in context.env:
        global react_map
        context.env[MONGO_SYNC_STATE] = 'init'
        create_reacts()
    else:
        return react_map[context.env[MONGO_SYNC_STATE]]

def dispatch(context):
    pass

def connect_to_mongo(context):
    global mongo_client
    mongo_client = MongoClient()
    print mongo_client
    context.env[MONGO_SYNC_STATE] = 'discover_data'

def discover_data_struct(context):
    for db in mongo_client.database_names():
        print 'database: ', db
        print mongo_client[db].collection_names(False)
    context.env[MONGO_SYNC_STATE] = 'finished'

def finished(context):
    context.env['status'] = RobbotState.ROBBOT_STATE_EXIT
    return True

def create_reacts():
    global react_map
    react_map = {'init': connect_to_mongo,
                 'finished': finished,
                 'discover_data': discover_data_struct}

    return react_map

__author__ = 'lin'
from react.reactor import *
from mongo.mongo_sync_react import register_mongo_reace



class DiscoverQueue(object):
    def __init__(self):
        self.discovers = []

    def push_discover(self, discover):
        self.discovers.append(discover)

    def pop_discover(self):
        discover = self.discovers.pop()
        return discover

    def next_discover(self):
        if len(self.discovers) > 0:
            return self.discovers[0]
        else:
            return None

    def count(self):
        return len(self.discovers)

class Context:
    def __init__(self, robbot):
        self.robbot = robbot
        self.states = None
        self.env = {}
        self.discoverQueue = DiscoverQueue()

class Robbot1(object):
    def __init__(self):
        pass

    def run(self):
        context = Context(self)
        react_stack = ReactStack()
        register_mongo_reace(react_stack)
        discover = Discover('init', {})
        react_with_current_context(None, react_stack, discover, context)

def init(state, discover, context):
    print 'init'

if __name__ == '__main__':
    robbot = Robbot1()
    robbot.run()

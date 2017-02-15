__author__ = 'lin'

class ReactStack(object):
    def __init__(self):
        self.stack = {}

    def register_react(self, kind, react_handler):
        if kind not in self.stack:
            self.stack[kind] = []
        self.stack[kind].append(react_handler)

    def react_of_discover(self, state, discover, context):
        return self.stack[discover.kind()]

class Discover(object):
    def __init__(self, message, env):
        self.message = message
        self.env = env

    def kind(self):
        return self.message


def react_with_current_context(state, react_stack, discover=None, context=None):
    react_functions = react_stack.react_of_discover(state, discover, context)
    for react_fun in react_functions:
        react_fun(state, discover, context)





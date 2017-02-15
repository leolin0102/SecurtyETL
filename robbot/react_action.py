__author__ = 'lin'


def take_step(context, reactors):
    action = reactors(context)
    return action(context)

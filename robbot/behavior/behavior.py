__author__ = 'lin'

from enum import Enum

from robbot.env.task import Context, TaskQueue, TaskState, Task
class RobbotState(Enum):
    ROBBOT_STATE_INIT = 0
    ROBBOT_STATE_RUNNING = 1
    ROBBOT_STATE_EXIT = 200

def react_with_context(context):
    return react_dispatch(context)

def react_dispatch(context):
    if 'status' not in context.env:
        return start_up_react
    elif context.env['status'] == RobbotState.ROBBOT_STATE_EXIT:
        return stop_react
    else:
        context.env['status'] = RobbotState.ROBBOT_STATE_RUNNING
        return context.reactor(context)

def start_up_react(context):
    print 'start up'
    context.env['status'] = RobbotState.ROBBOT_STATE_INIT
    return True

def stop_react(context):
    print 'stop robbot'
    return False


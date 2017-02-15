__author__ = 'lin'
from enum import Enum

class Context:
    def __init__(self, robbot, reactor):
        self.robbot = robbot
        self.states = None
        self.env = {}
        self.tasksQueue = TaskQueue()
        self.reactor = reactor

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def push_task(self, task):
        self.tasks.append(task)

    def pop_task(self):
        task = self.tasks.pop()
        return task

    def next_task(self):
        if len(self.tasks) > 0:
            return self.tasks[0]
        else:
            return None

    def count(self):
        return len(self.tasks)

class TaskState(Enum):
    TASK_INIT = 0
    TASK_ON_PROCESSING = 1

class Task(object):
    def __init__(self, env, state=TaskState.TASK_INIT, action=None):
        self.env = env
        self.state = state
        self.action = action

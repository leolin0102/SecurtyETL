__author__ = 'lin'
from react_action import take_step
from env.task import Context
from behavior.behavior import react_with_context
from mongo.mongo_sync_react import get_react_with_context

class Robbot:
    def __init__(self):
        self.context = Context(self, get_react_with_context)

    def take_step(self):
        if self.context.tasksQueue.count() > 0:
            task = self.context.tasksQueue.pop_task()
            task.action(self.context)
        else:
            react = react_with_context(self.context)
            if react is not None:
                return react(self.context)

    def run(self):
        while True:
            result = self.take_step()
            if result is False:
                break


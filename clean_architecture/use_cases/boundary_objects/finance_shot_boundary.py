from datetime import datetime


class FinanceShotBoundary(object):

    def __init__(self):
        self.id = int()
        self.created = datetime.now()
        self.title = str()
        self.description = str()
        self.cost = int()
        self.budget = int()
        self.title = 'no_title'
        self._title_is_correct = True

    @property
    def title_is_correct(self):
        return self._title_is_correct

    @title_is_correct.setter
    def title_is_correct(self, value):
        self._title_is_correct = value


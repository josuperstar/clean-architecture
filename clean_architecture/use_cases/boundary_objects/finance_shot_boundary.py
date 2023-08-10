from datetime import datetime


class FinanceShotBoundary(object):

    def __init__(self):
        self.id = int()
        self.created = datetime.now()
        self.title = str()
        self.description = str()
        self.cost = int()
        self.budget = int()
        self.title = str()
        self.is_over_budget = bool()


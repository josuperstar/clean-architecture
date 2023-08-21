from datetime import datetime


class ShotEntity(object):

    def __init__(self):
        self.id = int()
        self.created = datetime
        self.cost = 0
        self.budget = 0
        self.title = str()
        self.description = str()
        self.assets = list()

    def check_if_title_is_unique(self, existing_shots):
        for shot in existing_shots:
            if shot.title == self.title:
                return False
        return True

    def title_sanity_check(self):
        if ' ' in self.title:
            return False
        return True

    def is_over_budget(self):
        return self.cost > self.budget

    def __str__(self):
        return "{} {} {} {} {}".format(
            self.id,
            self.title,
            self.created,
            self.cost,
            self.budget
        )

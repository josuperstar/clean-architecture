from datetime import datetime


class ShotBoundary(object):
    id: int
    created: datetime
    title: str
    description: str

    def __init__(self):
        self.title = 'no_title'
        self._title_is_correct = True

    @property
    def title_is_correct(self):
        return self._title_is_correct

    @title_is_correct.setter
    def title_is_correct(self, value):
        self._title_is_correct = value

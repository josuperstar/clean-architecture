from datetime import datetime


class AssetBoundary(object):
    id: int
    created: datetime
    name: str
    description: str

    def __init__(self):
        self.name = 'no_name'
        self._name_is_correct = True

    @property
    def name_is_correct(self):
        return self._name_is_correct

    @name_is_correct.setter
    def name_is_correct(self, value):
        self._name_is_correct = value

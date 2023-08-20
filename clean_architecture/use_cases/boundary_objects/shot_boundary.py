from datetime import datetime
from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary


class ShotBoundary(object):
    id: int
    created: datetime
    title: str
    description: str

    def __init__(self):
        self.title = 'no_title'
        self._title_is_correct = True
        self.assets = list()

    @property
    def title_is_correct(self):
        return self._title_is_correct

    @title_is_correct.setter
    def title_is_correct(self, value):
        self._title_is_correct = value


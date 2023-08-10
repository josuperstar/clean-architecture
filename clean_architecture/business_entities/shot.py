from datetime import datetime


class ShotEntity(object):
    id: int
    created: datetime
    cost: int
    budget: int
    title: str
    description: str

    def check_if_title_is_unique(self, existing_shots):
        for shot in existing_shots:
            if shot.title == self.title:
                return False
        return True

    def title_sanity_check(self):
        if ' ' in self.title:
            return False
        return True

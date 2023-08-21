from datetime import datetime


class AssetEntity(object):

    def __init__(self):
        self.id = int()
        self.created = datetime
        self.cost = 0
        self.name = str()
        self.description = str()

    def check_if_name_is_unique(self, existing_assets):
        for asset in existing_assets:
            if asset.name == self.name:
                return False
        return True

    def name_sanity_check(self):
        if ' ' in self.name:
            return False
        return True

    def __str__(self):
        return "{} {} {} {}".format(
            self.id,
            self.name,
            self.created,
            self.cost
        )

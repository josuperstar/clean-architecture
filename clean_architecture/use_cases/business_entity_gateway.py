class BusinessEntityGateway(object):

    def get_asset(self, asset_id):
        raise NotImplemented

    def get_asset_list(self):
        raise NotImplemented

    def update_asset(self, asset):
        raise NotImplemented

    def delete_asset(self, asset):
        raise NotImplemented

    def get_shot(self, shot_id):
        pass

    def get_shot_list(self):
        pass

    def create_shot(self, shot):
        pass

    def update_shot(self, shot):
        pass

    def delete_shot(self, shot_id):
        pass

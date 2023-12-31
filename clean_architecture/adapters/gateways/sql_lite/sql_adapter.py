
from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.business_entities.asset import AssetEntity


class SqlGateway(BusinessEntityGateway):

    def get_connection(self):
        raise NotImplemented

    def get_asset(self, asset_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        print('get asset')
        asset_result = connection.execute('SELECT * FROM assets WHERE id = ?',
                            (asset_id,)).fetchone()
        connection.close()
        if asset_result is None:
            return None

        asset = AssetEntity()
        asset.id = asset_result['id']
        asset.created = asset_result['created']
        asset.name = asset_result['name']
        asset.description = asset_result['description']
        asset.cost = asset_result['cost']

        return asset

    def get_asset_list(self):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        print('get asset')
        assets_result = connection.execute('SELECT * FROM assets').fetchall()
        connection.close()
        assets = list()
        for asset_result in assets_result:
            asset = AssetEntity()
            asset.id = asset_result['id']
            asset.created = asset_result['created']
            asset.name = asset_result['name']
            asset.description = asset_result['description']
            asset.cost = asset_result['cost']
            assets.append(asset)
        return assets

    def create_asset(self, asset):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('INSERT INTO assets (name, description, cost) VALUES (?, ?, ?)',
                     (asset.name, asset.description, 0))
        connection.commit()
        connection.close()

    def update_asset(self, asset):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('UPDATE assets SET name = ?, description = ?'
                     ' WHERE id = ?',
                     (asset.name, asset.description, asset.id))
        connection.commit()
        connection.close()

    def delete_asset(self, asset):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('DELETE FROM assets WHERE id = ?', (asset.id,))
        connection.commit()
        connection.close()

    def get_shot(self, shot_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        print('get shot')
        post_result = connection.execute('SELECT * FROM shots WHERE id = ?',
                            (shot_id,)).fetchone()
        connection.close()
        if post_result is None:
            return None

        shot = ShotEntity()
        shot.id = post_result['id']
        shot.created = post_result['created']
        shot.title = post_result['title']
        shot.description = post_result['description']
        shot.cost = post_result['cost']
        shot.budget = post_result['budget']

        return shot

    def get_shot_list(self):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        posts_result = connection.execute('SELECT * FROM shots').fetchall()
        connection.close()
        shots = list()
        for shot_result in posts_result:
            print(shot_result)
            shot = ShotEntity()
            shot.id = shot_result['id']
            shot.created = shot_result['created']
            shot.title = shot_result['title']
            shot.description = shot_result['description']
            shot.cost = shot_result['cost']
            shot.budget = shot_result['budget']

            shots.append(shot)
        return shots

    def get_assets_by_shot(self, shot_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')

        query = """
        SELECT assets.id, assets.name, assets.created, assets.description, assets.cost FROM assets
        JOIN shot_asset_relationships ON assets.id = asset_reference
        JOIN shots ON shot_asset_relationships.shot_reference = shots.id
        WHERE assets.id = {};
        """.format(shot_id)
        posts_result = connection.execute(query).fetchall()
        connection.close()
        assets = list()
        for asset_result in posts_result:
            print(asset_result)
            asset = AssetEntity()
            asset.id = asset_result['id']
            asset.created = asset_result['created']
            asset.name = asset_result['name']
            asset.description = asset_result['description']
            asset.cost = asset_result['cost']
            assets.append(asset)
        return assets

    def get_shots_by_asset(self, asset_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')

        query = """
        SELECT shots.id, title, shots.description, shots.cost, shots.created, budget FROM shots
        JOIN shot_asset_relationships ON shots.id = shot_reference
        JOIN assets ON shot_asset_relationships.asset_reference = assets.id
        WHERE assets.id = {}
        ORDER BY title;
        """.format(asset_id)
        posts_result = connection.execute(query).fetchall()
        connection.close()
        shots = list()
        for shot_result in posts_result:
            print(shot_result)
            shot = ShotEntity()
            shot.id = shot_result['id']
            shot.created = shot_result['created']
            shot.title = shot_result['title']
            shot.description = shot_result['description']
            shot.cost = shot_result['cost']
            shot.budget = shot_result['budget']

            shots.append(shot)
        return shots

    def create_shot(self, shot):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('INSERT INTO shots (title, description, budget, cost) VALUES (?, ?, ?, ?)',
                     (shot.title, shot.description, 0, 0))
        connection.commit()
        connection.close()

    def update_shot(self, shot):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('UPDATE shots SET title = ?, description = ?'
                     ' WHERE id = ?',
                     (shot.title, shot.description, shot.id))
        connection.commit()
        connection.close()

    def delete_shot(self, shot):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('DELETE FROM shots WHERE id = ?', (shot.id,))
        connection.commit()
        connection.close()

    def link_shot_to_asset(self, asset_id, shot_id):

        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        connection.execute('INSERT INTO shot_asset_relationships (shot_reference, asset_reference) VALUES (?, ?)',
                     (shot_id, asset_id))
        connection.commit()
        connection.close()

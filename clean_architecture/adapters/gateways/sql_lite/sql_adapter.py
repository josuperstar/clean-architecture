
from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.business_entities.shot import ShotEntity


class SqlGateway(BusinessEntityGateway):

    def get_connection(self):
        raise NotImplemented

    def get_asset(self, asset_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        print('get shot')
        asset_result = connection.execute('SELECT * FROM assets WHERE id = ?',
                            (asset_id,)).fetchone()
        connection.close()
        if asset_result is None:
            return None

        shot = ShotEntity()
        shot.id = asset_result['id']
        shot.created = asset_result['created']
        shot.title = asset_result['name']
        shot.description = asset_result['description']
        shot.cost = asset_result['cost']

        return shot

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

    def get_shot_by_asset(self, asset_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')

        query = """
        SELECT shots.id, title, shots.description, shots.cost, shots.created, budget FROM shots
        JOIN shot_asset_relationships ON shots.id = shot_reference
        JOIN assets ON shot_asset_relationships.asset_reference = assets.id
        ORDER BY title;
        """
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

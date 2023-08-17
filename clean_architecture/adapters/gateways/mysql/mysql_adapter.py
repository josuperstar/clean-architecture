from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.business_entities.shot import ShotEntity


class MySqlGateway(BusinessEntityGateway):

    def get_db_connection(self):
        raise NotImplemented

    def get_shot(self, shot_id):
        print('get shot')
        connection = self.get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM element WHERE id = %s',
                            (shot_id,))
        shot_result = cursor.fetchone()
        connection.close()
        if shot_result is None:
            return None

        post = ShotEntity()
        post.id = shot_result[0]
        post.created = shot_result[1]
        post.title = shot_result[2]
        post.description = shot_result[3]
        if shot_result[4]:
            post.cost = shot_result[4]
        if shot_result[5]:
            post.budget = shot_result[5]

        return post

    def get_shot_list(self):

        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM element')
        shots_result = cursor.fetchall()
        conn.close()
        shots = list()
        for shot_result in shots_result:
            print(shot_result)
            shot = ShotEntity()
            shot.id = shot_result[0]
            shot.created = shot_result[1]
            shot.title = shot_result[2]
            shot.description = shot_result[3]
            if shot_result[4]:
                shot.cost = shot_result[4]
            if shot_result[5]:
                shot.budget = shot_result[5]
            shots.append(shot)
        return shots

    def create_shot(self, shot):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO element (name, content) VALUES (%s, %s)',
                     (shot.title, shot.description))
        conn.commit()
        conn.close()

    def update_shot(self, shot):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE element SET name = %s, content = %s'
                     ' WHERE id = %s',
                     (shot.title, shot.description, shot.id))
        conn.commit()
        conn.close()

    def delete_shot(self, shot):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM element WHERE id = %s', (shot.id,))
        conn.commit()
        conn.close()

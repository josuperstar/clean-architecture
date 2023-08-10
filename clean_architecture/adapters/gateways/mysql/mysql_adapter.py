from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.business_entities.shot import ShotEntity


class MySqlGateway(BusinessEntityGateway):

    def get_db_connection(self):
        raise NotImplemented

    def get_shot(self, shot_id):
        print('get post')
        connection = self.get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM element WHERE id = %s',
                            (shot_id,))
        post_result = cursor.fetchone()
        connection.close()
        if post_result is None:
            return None

        post = ShotEntity()
        post.id = post_result[0]
        post.created = post_result[1]
        post.title = post_result[2]
        post.description = post_result[3]
        post.cost = post_result[4]
        post.budget = post_result[5]

        return post

    def get_shot_list(self):

        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM element')
        posts_result = cursor.fetchall()
        conn.close()
        posts = list()
        for post_result in posts_result:
            print(post_result)
            post = ShotEntity()
            post.id = post_result[0]
            post.created = post_result[1]
            post.title = post_result[2]
            post.description = post_result[3]
            post.cost = post_result[4]
            post.budget = post_result[5]
            posts.append(post)
        return posts

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
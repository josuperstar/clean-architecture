
from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.business_entities.shot import ShotEntity


class SqlGateway(BusinessEntityGateway):

    def get_connection(self):
        raise NotImplemented

    def get_shot(self, shot_id):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        print('get post')
        post_result = connection.execute('SELECT * FROM shots WHERE id = ?',
                            (shot_id,)).fetchone()
        connection.close()
        if post_result is None:
            return None

        post = ShotEntity()
        post.id = post_result['id']
        post.created = post_result['created']
        post.title = post_result['title']
        post.description = post_result['description']
        post.cost = post_result['cost']
        post.budget = post_result['budget']

        return post

    def get_shot_list(self):
        connection = self.get_connection()
        if not connection:
            raise Exception('connection not instantiated.')
        posts_result = connection.execute('SELECT * FROM shots').fetchall()
        connection.close()
        posts = list()
        for post_result in posts_result:
            print(post_result)
            post = ShotEntity()
            post.id = post_result['id']
            post.created = post_result['created']
            post.title = post_result['title']
            post.description = post_result['description']
            post.cost = post_result['cost']
            post.budget = post_result['budget']

            posts.append(post)
        return posts

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

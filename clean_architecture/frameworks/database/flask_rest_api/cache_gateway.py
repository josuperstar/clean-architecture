import os
import sqlite3

from clean_architecture.adapters.gateways.sql_lite.sql_adapter import SqlGateway
from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.frameworks.database.flask_rest_api.database_cache import FlaskCachingDatabase


class FlaskCacheGateway(SqlGateway):

    def __init__(self):
        super().__init__()
        self._cached_database = FlaskCachingDatabase(self)

    def get_connection(self):
        print('get sql lite db connection')
        directory = os.path.dirname(__file__)
        database = r"{}\database.db".format(directory)
        connection = sqlite3.connect(database)
        connection.row_factory = sqlite3.Row
        return connection

    def get_shot(self, shot_id):
        print('getting shot with rest api')
        import requests
        url = "http://127.0.0.1:8000/{}".format(shot_id)
        response = requests.get(url)
        result = response.json()
        print('converting dict into entity class')
        shot = ShotEntity()
        shot.id = result['id']
        shot.title = result['title']
        shot.description = result['description']
        return shot

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

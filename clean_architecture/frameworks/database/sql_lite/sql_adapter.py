import os

import sqlite3

from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.business_entities.shot import ShotEntity


def get_db_connection():
    print('get sqllite db connection')
    directory = os.path.dirname(__file__)
    database = r"{}\database.db".format(directory)
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn


class SqlGateway(BusinessEntityGateway):

    def get_shot(self, shot_id):
        print('get post')
        conn = get_db_connection()
        post_result = conn.execute('SELECT * FROM shots WHERE id = ?',
                            (shot_id,)).fetchone()
        conn.close()
        if post_result is None:
            return None

        post = ShotEntity()
        post.id = post_result['id']
        post.created = post_result['created']
        post.title = post_result['title']
        post.description = post_result['description']

        return post

    def get_post_list(self):

        conn = get_db_connection()
        posts_result = conn.execute('SELECT * FROM shots').fetchall()
        conn.close()
        posts = list()
        for post_result in posts_result:
            print(post_result)
            post = ShotEntity()
            post.id = post_result['id']
            post.created = post_result['created']
            post.title = post_result['title']
            post.description = post_result['description']
            posts.append(post)
        return posts

    def create_shot(self, shot):
        conn = get_db_connection()
        conn.execute('INSERT INTO shots (title, description) VALUES (?, ?)',
                     (shot.title, shot.description))
        conn.commit()
        conn.close()

    def update_shot(self, shot):
        conn = get_db_connection()
        conn.execute('UPDATE shots SET title = ?, description = ?'
                     ' WHERE id = ?',
                     (shot.title, shot.description, shot.id))
        conn.commit()
        conn.close()

    def delete_shot(self, shot_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM shots WHERE id = ?', (shot_id,))
        conn.commit()
        conn.close()

import os

import sqlite3

from clean_architecture.adapters.ORM.post import PostModel
from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway


def get_db_connection():
    print('get db connection')
    directory = os.path.dirname(__file__)
    database = r"{}\database.db".format(directory)
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn


class SqlGateway(BusinessEntityGateway):

    def get_post(self, post_id):
        print('get post')
        conn = get_db_connection()
        post_result = conn.execute('SELECT * FROM posts WHERE id = ?',
                            (post_id,)).fetchone()
        conn.close()
        if post_result is None:
            return None

        post = PostModel()
        post.id = post_result['id']
        post.created = post_result['created']
        post.title = post_result['title']
        post.content = post_result['content']

        return post

    def get_post_list(self):

        conn = get_db_connection()
        posts_result = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        posts = list()
        for post_result in posts_result:
            print(post_result)
            post = PostModel()
            post.id = post_result['id']
            post.created = post_result['created']
            post.title = post_result['title']
            post.content = post_result['content']
            posts.append(post)
        return posts

    def create_post(self, post):
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                     (post.title, post.content))
        conn.commit()
        conn.close()

    def update_post(self, post):
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?'
                     ' WHERE id = ?',
                     (post.title, post.content, post.id))
        conn.commit()
        conn.close()

    def delete_post(self, post_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        conn.commit()
        conn.close()

import sqlite3

from model.post import Post


def get_db_connection():
    print('get db connection')
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    print('get post')
    conn = get_db_connection()
    post_result = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post_result is None:
        return None

    post = Post()
    post.id = post_result['id']
    post.created = post_result['created']
    post.title = post_result['title']
    post.content = post_result['content']

    return post


def get_post_list():

    conn = get_db_connection()
    posts_result = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    posts = list()
    for post_result in posts_result:
        print(post_result)
        post = Post()
        post.id = post_result['id']
        post.created = post_result['created']
        post.title = post_result['title']
        post.content = post_result['content']
        posts.append(post)
    return posts


def create_post(post):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (post.title, post.content))
    conn.commit()
    conn.close()


def update_post(post):
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ?'
                 ' WHERE id = ?',
                 (post.title, post.content, post.id))
    conn.commit()
    conn.close()

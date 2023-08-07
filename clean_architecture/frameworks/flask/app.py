from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from clean_architecture.adapters.sql_adapter import (get_post_list,
                                                     get_post,
                                                     get_db_connection,
                                                     create_post,
                                                     update_post)
from clean_architecture.adapters.ORM.post import Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    posts = get_post_list()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post()
        post.title = title
        post.content = content
        if not title:
            flash('Title is required!')
        else:
            create_post(post)
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post()
        post.id = id
        post.title = title
        post.content = content
        if not title:
            flash('Title is required!')
        else:
            update_post(post)
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

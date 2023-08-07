from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


from clean_architecture.use_cases.list_post_use_case import ListPostUseCases
from clean_architecture.adapters.ORM.post import PostModel
from clean_architecture.adapters.presenters.post import PostPresenter
from clean_architecture.adapters.sql_adapter import SqlGateway

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
database = SqlGateway()


def boundary_to_presenter(boundary):
    presenter = PostPresenter()
    presenter.id = boundary.id
    presenter.title = boundary.title
    presenter.content = boundary.content
    presenter.title_size = 'h3'
    return presenter

@app.route('/')
def index():
    list_post = ListPostUseCases(database)
    posts = list_post.execute()
    list_of_presenters = list()
    for post in posts:
        presenter = boundary_to_presenter(post)
        list_of_presenters.append(presenter)
    return render_template('index.html', posts=list_of_presenters)


@app.route('/<int:post_id>')
def post(post_id):
    post = database.get_post(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = PostModel()
        post.title = title
        post.content = content
        if not title:
            flash('Title is required!')
        else:
            database.create_post(post)
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = database.get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = PostModel()
        post.id = id
        post.title = title
        post.content = content
        if not title:
            flash('Title is required!')
        else:
            database.update_post(post)
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = database.get_post(id)
    database.delete_post(id)
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

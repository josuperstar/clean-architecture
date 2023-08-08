from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from clean_architecture.use_cases.create_shot_use_case import CreateShotUseCases
from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.frameworks.database.sql_lite.sql_adapter import SqlGateway
from clean_architecture.adapters.controllers.shot_controller import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
database = SqlGateway()


@app.route('/')
def index():
    shot_controller = ShotController(database)
    list_of_presenters = shot_controller.get_shot_list()
    return render_template('index.html', posts=list_of_presenters)


@app.route('/<int:post_id>')
def post(post_id):
    post = database.get_shot(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        shot_info = ShotEntity()
        title = request.form['title']
        shot_info.title = title
        if not title:
            flash('Title is required!')
        else:
            description = request.form['description']
            shot_info.description = description
            create_shot = CreateShotUseCases(database)
            create_shot.set_shot_info(shot_info)
            try:
                create_shot.execute()
                return redirect(url_for('index'))
            except Exception as e:
                flash(e)

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = database.get_shot(id)

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        post = ShotEntity()
        post.id = id
        post.title = title
        post.description = description
        if not title:
            flash('Title is required!')
        else:
            database.update_shot(post)
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = database.get_shot(id)
    database.delete_shot(id)
    flash('"{}" was successfully deleted!'.format(post.title))
    return redirect(url_for('index'))

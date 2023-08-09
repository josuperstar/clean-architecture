import os
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import configparser

from clean_architecture.business_entities.shot import ShotEntity

from clean_architecture.use_cases.shot_management.create_shot_use_case import CreateShotUseCases
from clean_architecture.use_cases.shot_management.update_shot_use_case import UpdateShotUseCases
from clean_architecture.use_cases.shot_management.delete_shot_use_case import DeleteShotUseCases

from clean_architecture.adapters.controllers.shot_controller import *

from clean_architecture.frameworks.database.sql_lite.sql_adapter import SqlGateway
from clean_architecture.frameworks.database.mysql.mysql_adapter import MySqlGateway


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Read config file to get the right database
config = configparser.ConfigParser()
directory = os.path.dirname(__file__)
config_file = r"{}\config.ini".format(directory)
config.read(config_file)
database_info = config['database']
database_name = database_info.get('name')
if database_name == 'sqllite':
    database = SqlGateway()
elif database_name == 'mysql':
    database = MySqlGateway()
else:
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
    shot = database.get_shot(id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        shot = ShotEntity()
        shot.id = id
        shot.title = title
        shot.description = description
        if not title:
            flash('Title is required!')
        else:

            update_shot = UpdateShotUseCases(database)
            update_shot.set_shot_info(shot)
            update_shot.execute()
            return redirect(url_for('index'))

    return render_template('edit.html', post=shot)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    shot = database.get_shot(id)
    delete_shot = DeleteShotUseCases(database)
    delete_shot.set_shot_info(shot)
    delete_shot.execute()
    flash('"{}" was successfully deleted!'.format(shot.title))
    return redirect(url_for('index'))

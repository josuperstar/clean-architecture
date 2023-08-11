from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from clean_architecture.adapters.controllers.shot_controller import *
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase


class FlaskAppWrapper(object):

    def __init__(self, database):
        flask_app = Flask(__name__)
        self.app = flask_app
        self.app.config['SECRET_KEY'] = 'your secret key'
        self._database = database
        self.shot_controller = ShotController(database)

        @self.app.route('/')
        def index():
            list_of_presenters = self.shot_controller.get_shot_list()
            return render_template('index.html', posts=list_of_presenters)

        @self.app.route('/accounting')
        def accounting():
            list_of_presenters = self.shot_controller.get_shot_list_with_financial_data()
            return render_template('accounting_index.html', posts=list_of_presenters)

        @self.app.route('/accounting/<int:post_id>')
        def accounting_shot(post_id):
            shot = self.shot_controller.get_finance_shot(post_id)
            if shot is None:
                abort(404)
            return render_template('accounting_shot.html', post=shot)

        @self.app.route('/<int:post_id>')
        def post(post_id):
            shot = self.shot_controller.get_shot(post_id)
            if shot is None:
                abort(404)
            return render_template('post.html', post=shot)

        @self.app.route('/create', methods=('GET', 'POST'))
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
                    try:
                        self.shot_controller.create_shot(shot_info)
                        return redirect(url_for('index'))
                    except Exception as e:
                        flash(e)

            return render_template('create.html')

        @self.app.route('/<int:id>/edit', methods=('GET', 'POST'))
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
                    self.shot_controller.update_shot(shot)
                    return redirect(url_for('index'))

            return render_template('edit.html', post=shot)

        @self.app.route('/<int:id>/delete', methods=('POST',))
        def delete(id):
            shot_info = self.shot_controller.get_shot(id)
            self.shot_controller.delete_shot(shot_info)
            flash('"{}" was successfully deleted!'.format(shot_info.title))
            return redirect(url_for('index'))

    def run(self, **kwargs):
        self.app.run(**kwargs)


if __name__ == "__main__":

    database = SqlLiteDatabase()
    app = FlaskAppWrapper(database)
    app.run(debug=True)

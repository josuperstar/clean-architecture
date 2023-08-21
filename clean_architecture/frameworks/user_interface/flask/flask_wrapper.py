from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from clean_architecture.adapters.controllers.shot_controller import *


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
            return render_template('index.html', shots=list_of_presenters)

        @self.app.route('/accounting')
        def accounting():
            list_of_presenters = self.shot_controller.get_shot_list_with_financial_data()
            return render_template('accounting_index.html', shots=list_of_presenters)

        @self.app.route('/assets')
        def assets():
            list_of_presenters = self.shot_controller.get_asset_list()
            return render_template('asset_list.html', assets=list_of_presenters)

        @self.app.route('/accounting/<int:shot_id>')
        def accounting_shot(shot_id):
            shot = self.shot_controller.get_finance_shot(shot_id)
            if shot is None:
                abort(404)
            return render_template('accounting_shot.html', shot=shot)

        @self.app.route('/<int:shot_id>')
        def shot(shot_id):
            shot = self.shot_controller.get_shot(shot_id)
            if shot is None:
                abort(404)
            return render_template('shot.html', shot=shot)

        @self.app.route('/asset/<int:asset_id>')
        def asset(asset_id):
            asset = self.shot_controller.get_asset(asset_id)
            if asset is None:
                abort(404)
            return render_template('asset.html', asset=asset)

        @self.app.route('/create_shot', methods=('GET', 'POST'))
        def create_shot():
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

            return render_template('create_shot.html')

        @self.app.route('/create_asset', methods=('GET', 'POST'))
        def create_asset():
            if request.method == 'POST':
                asset_info = AssetEntity()
                title = request.form['title']
                asset_info.name = title
                if not title:
                    flash('Title is required!')
                else:
                    description = request.form['description']
                    asset_info.description = description
                    try:
                        self.shot_controller.create_asset(asset_info)
                        return redirect(url_for('assets'))
                    except Exception as e:
                        flash(e)

            return render_template('create_asset.html')

        @self.app.route('/assets/<int:id>/edit_asset', methods=('GET', 'POST'))
        def edit_asset(id):
            asset = self.shot_controller.get_asset(id)
            if request.method == 'POST':
                name = request.form['name']
                description = request.form['description']
                asset = AssetEntity()
                asset.id = id
                asset.name = name
                asset.description = description
                if not name:
                    flash('Name is required!')
                else:
                    self.shot_controller.update_asset(asset)
                    return redirect(url_for('assets'))

            return render_template('assets/edit_asset.html', asset=asset)

        @self.app.route('/assets/<int:id>/delete_asset', methods=('POST',))
        def delete_asset(id):
            asset_info = self.shot_controller.get_asset(id)
            self.shot_controller.delete_asset(asset_info)
            flash('"{}" was successfully deleted!'.format(asset_info.name))
            return redirect(url_for('assets'))

        @self.app.route('/<int:id>/edit_shot', methods=('GET', 'POST'))
        def edit_shot(id):
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

            return render_template('edit_shot.html', shot=shot)

        @self.app.route('/<int:id>/delete', methods=('POST',))
        def delete(id):
            shot_info = self.shot_controller.get_shot(id)
            self.shot_controller.delete_shot(shot_info)
            flash('"{}" was successfully deleted!'.format(shot_info.title))
            return redirect(url_for('index'))

    def run(self, **kwargs):
        self.app.run(**kwargs)


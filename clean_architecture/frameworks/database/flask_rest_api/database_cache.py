from flask import Flask
from flask_caching import Cache
from werkzeug.exceptions import abort

from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase


class FlaskCachingDatabase(object):

    def __init__(self, database):
        flask_app = Flask(__name__)
        self.app = flask_app
        # self.app.config['SECRET_KEY'] = 'your secret key'
        config = {
            "CACHE_TYPE": "SimpleCache",  # caching type
            "CACHE_DEFAULT_TIMEOUT": 300  # default Cache Timeout
        }
        # Flask to use the above defined config
        self.app.config.from_mapping(config)
        self.cache = Cache(self.app)
        self.cache.init_app(self.app)
        self._database = database

        @self.app.route('/<int:shot_id>')
        @self.cache.cached(timeout=50)
        def post(shot_id):
            print('=================== CACHE SERVER ==================')
            print('getting real request')
            shot: ShotEntity
            shot = self._database.get_shot(shot_id)
            if shot is None:
                abort(404)
            shot_dictionary = dict()
            shot_dictionary['id'] = shot.id
            shot_dictionary['title'] = shot.title
            shot_dictionary['description'] = shot.description

            print('result: {}'.format(shot_dictionary))

            return shot_dictionary

    def run(self, **kwargs):
        self.app.run(**kwargs)


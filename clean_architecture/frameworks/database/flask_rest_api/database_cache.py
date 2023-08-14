from flask import Flask, render_template
from flask_caching import Cache
from werkzeug.exceptions import abort

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
            print('getting real request')
            shot = self._database.get_shot(shot_id)
            if shot is None:
                abort(404)
            return render_template('shot.html', post=shot)

    def run(self, **kwargs):
        self.app.run(**kwargs)


if __name__ == "__main__":

    database = SqlLiteDatabase()
    app = FlaskCachingDatabase(database)
    app.run(debug=True, port=8000)

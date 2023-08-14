import threading

from clean_architecture.frameworks.user_interface.flask.flask_wrapper import FlaskAppWrapper

from clean_architecture.frameworks.database.flask_rest_api.cache_gateway import FlaskCacheGateway
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase
from clean_architecture.frameworks.database.flask_rest_api.cache_gateway import FlaskCachingDatabase


if __name__ == "__main__":

    database = SqlLiteDatabase()
    database_server_app = FlaskCachingDatabase(database)
    threading.Thread(target=lambda: database_server_app.run(threaded=True, port=8000)).start()

    database = FlaskCacheGateway()
    app = FlaskAppWrapper(database)
    app.run(threaded=True, port=5000)

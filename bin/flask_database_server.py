
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase
from clean_architecture.frameworks.database.flask_rest_api.cache_gateway import FlaskCachingDatabaseServer


if __name__ == "__main__":

    database = SqlLiteDatabase()
    database_server_app = FlaskCachingDatabaseServer(database)
    database_server_app.run(threaded=True, port=8000)

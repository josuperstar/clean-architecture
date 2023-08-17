
from clean_architecture.frameworks.user_interface.flask.flask_wrapper import FlaskAppWrapper
from clean_architecture.frameworks.database.database_factory import DatabaseFactory


if __name__ == "__main__":

    factory = DatabaseFactory()
    database = factory.create_database('sqllite', with_caching=True)
    app = FlaskAppWrapper(database)
    app.run(threaded=True, port=5000)

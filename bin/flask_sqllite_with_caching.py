
from clean_architecture.frameworks.user_interface.flask.flask_wrapper import FlaskAppWrapper

from clean_architecture.frameworks.database.flask_rest_api.cache_gateway import FlaskCacheGateway


if __name__ == "__main__":

    database = FlaskCacheGateway()

    app = FlaskAppWrapper(database)
    app.run(debug=True)

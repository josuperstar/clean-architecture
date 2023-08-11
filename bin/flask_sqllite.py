
from clean_architecture.frameworks.user_interface.flask.flask_wrapper import FlaskAppWrapper
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase

if __name__ == "__main__":
    database = SqlLiteDatabase()
    app = FlaskAppWrapper(database)
    app.run(debug=True)

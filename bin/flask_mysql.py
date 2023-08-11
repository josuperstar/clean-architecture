
from clean_architecture.frameworks.user_interface.flask.flask_wrapper import FlaskAppWrapper
from clean_architecture.frameworks.database.mysql.mysql_database import MySqlDatabase

if __name__ == "__main__":
    database = MySqlDatabase()
    app = FlaskAppWrapper(database)
    app.run(debug=True)

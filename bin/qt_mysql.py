from clean_architecture.frameworks.database.mysql.mysql_database import MySqlDatabase
from clean_architecture.frameworks.user_interface.qt.app import QtShotApplication

if __name__ == '__main__':

    database = MySqlDatabase()
    qt_application = QtShotApplication(database)

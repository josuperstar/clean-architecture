from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase
from clean_architecture.frameworks.user_interface.qt.app import QtShotApplication

if __name__ == '__main__':

    database = SqlLiteDatabase()
    qt_application = QtShotApplication(database)

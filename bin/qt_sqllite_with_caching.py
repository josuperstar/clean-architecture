from clean_architecture.frameworks.database.database_factory import DatabaseFactory
from clean_architecture.frameworks.user_interface.qt.app import QtShotApplication

if __name__ == '__main__':
    factory = DatabaseFactory()
    database = factory.create_database('sqllite', with_caching=True)
    qt_application = QtShotApplication(database)

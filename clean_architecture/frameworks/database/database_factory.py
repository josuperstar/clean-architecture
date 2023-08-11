from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.frameworks.database.mysql.mysql_database import MySqlDatabase
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase


class DatabaseFactory(object):
    def create_database(self, database_name) -> BusinessEntityGateway:
        if database_name == 'mysql':
            return self._create_mysql()
        elif database_name == 'sqllite':
            return self._create_sqllite()

    @staticmethod
    def _create_mysql() -> BusinessEntityGateway:
        database = MySqlDatabase()
        return database

    @staticmethod
    def _create_sqllite() -> BusinessEntityGateway:
        database = SqlLiteDatabase()
        return database

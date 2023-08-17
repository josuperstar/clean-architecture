from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway
from clean_architecture.frameworks.database.mysql.mysql_database import MySqlDatabase
from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase
from clean_architecture.frameworks.database.flask_rest_api.cache_gateway import FlaskCacheGateway


class DatabaseFactory(object):
    def create_database(self, database_name, with_caching=False) -> BusinessEntityGateway:
        if database_name == 'mysql':
            return self._create_mysql(with_caching)
        elif database_name == 'sqllite':
            return self._create_sqllite(with_caching)

    @staticmethod
    def _create_mysql(with_caching) -> BusinessEntityGateway:
        database = MySqlDatabase()
        return database

    @staticmethod
    def _create_sqllite(with_caching) -> BusinessEntityGateway:
        if with_caching:
            database = FlaskCacheGateway()
        else:
            database = SqlLiteDatabase()
        return database

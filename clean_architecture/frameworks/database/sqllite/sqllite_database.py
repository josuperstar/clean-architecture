import os

import sqlite3

from clean_architecture.adapters.gateways.sql_lite.sql_adapter import SqlGateway


class SqlLiteDatabase(SqlGateway):

    def get_connection(self):
        print('get sql lite db connection')
        directory = os.path.dirname(__file__)
        database = r"{}\database.db".format(directory)
        connection = sqlite3.connect(database)
        connection.row_factory = sqlite3.Row
        return connection

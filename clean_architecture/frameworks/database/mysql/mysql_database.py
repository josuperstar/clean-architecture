import os

import mysql.connector
import configparser
from clean_architecture.adapters.gateways.mysql.mysql_adapter import MySqlGateway


class MySqlDatabase(MySqlGateway):

    def get_db_connection(self):
        print('get mysql db connection')
        config = configparser.ConfigParser()
        directory = os.path.dirname(__file__)
        config_file = r"{}\config.ini".format(directory)
        config.read(config_file)
        database_info = config['database']
        print(database_info)
        connection = mysql.connector.connect(host="localhost",
                                             user=database_info['username'],
                                             password=database_info['password'],
                                             database=database_info['name'])
        return connection

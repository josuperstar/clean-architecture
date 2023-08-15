import os
import sqlite3

from clean_architecture.adapters.gateways.sql_lite.sql_adapter import SqlGateway
from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.frameworks.database.flask_rest_api.cache_database_server import FlaskCachingDatabaseServer


class FlaskCacheGateway(SqlGateway):

    def __init__(self):
        super().__init__()
        self._cached_database = FlaskCachingDatabaseServer(self)
        self._database_server_url = "http://127.0.0.1:8000"

    def get_connection(self):
        print('get sql lite db connection')
        directory = os.path.dirname(__file__)
        database = r"{}\database.db".format(directory)
        connection = sqlite3.connect(database)
        connection.row_factory = sqlite3.Row
        return connection

    def get_shot(self, shot_id):
        print('getting shot with rest api')
        import requests
        url = "{}/{}".format(self._database_server_url, shot_id)
        try:
            response = requests.get(url)
            result = response.json()
        except ConnectionRefusedError as e:
            raise
        print('converting dict into entity class')
        shot = ShotEntity()
        shot.id = result['id']
        shot.title = result['title']
        shot.description = result['description']
        return shot

    def get_shot_list(self):
        shots = list()
        import requests
        url = "{}/shot_list".format(self._database_server_url)
        try:
            response = requests.get(url)
            result = response.json()
        except ConnectionRefusedError as e:
            raise
        for block in result:
            print('converting dict into entity class')
            shot = ShotEntity()
            shot.id = block['id']
            shot.title = block['title']
            shot.description = block['description']

            shots.append(shot)
        return shots

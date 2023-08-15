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
        shot = self.dictionary_to_shot(result)
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
        for shot_dictionary in result:
            print('converting dict into entity class')
            shot = self.dictionary_to_shot(shot_dictionary)
            shots.append(shot)
        return shots

    @staticmethod
    def dictionary_to_shot(shot_dictionary):
        shot_entity = ShotEntity()
        shot_entity.id = shot_dictionary['id']
        shot_entity.title = shot_dictionary['title']
        shot_entity.description = shot_dictionary['description']
        shot_entity.cost = shot_dictionary['cost']
        shot_entity.budget = shot_dictionary['budget']
        return shot_entity

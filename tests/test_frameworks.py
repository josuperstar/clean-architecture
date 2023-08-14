
import unittest

from clean_architecture.business_entities.shot import ShotEntity
from frameworks.database.sqllite.sqllite_database import SqlLiteDatabase


class Testing(unittest.TestCase):

    def test_get_shot(self):
        shot_id = 1
        sql = SqlLiteDatabase()
        shot: ShotEntity
        shot = sql.get_shot(shot_id)
        print(shot)

    def test_cached_shot(self):
        """
        This test works only when the flask database server is running
        with at least one shot in the database.
        """
        print('test cached shot')
        import requests
        shot_id = 1
        try:
            url = "http://127.0.0.1:8000/{}".format(shot_id)
            print('testing with URL {}'.format(url))
            response = requests.get(url)
            print(response.text)
        except ConnectionRefusedError as e:
            print('the database server is not running.')


if __name__ == '__main__':
    unittest.main()


import unittest

from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.frameworks.database.sql_lite.sql_adapter import SqlGateway


class Testing(unittest.TestCase):

    def test_get_shot(self):
        shot_id = 1
        sql = SqlGateway()
        shot: ShotEntity
        shot = sql.get_shot(shot_id)
        print(shot)


if __name__ == '__main__':
    unittest.main()


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


if __name__ == '__main__':
    unittest.main()

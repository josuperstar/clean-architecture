
import unittest

from clean_architecture.business_entities.shot import ShotEntity
from frameworks.database.sqllite.sqllite_database import SqlLiteDatabase


class Testing(unittest.TestCase):

    def test_get_asset(self):
        shot_id = 1
        sql = SqlLiteDatabase()
        shot: ShotEntity
        shot = sql.get_asset(shot_id)
        print(shot)

    def test_get_shot_by_asset(self):
        asset_id = 1
        sql = SqlLiteDatabase()

        shots = sql.get_shots_by_asset(asset_id)
        for shot in shots:
            print(shot.title)


if __name__ == '__main__':
    unittest.main()

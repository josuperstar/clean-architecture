
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

    def test_get_assets_by_shot(self):
        print('test get assets by shot')
        shot_id = 1
        sql = SqlLiteDatabase()

        assets = sql.get_assets_by_shot(shot_id)
        for asset in assets:
            print(asset.name)

if __name__ == '__main__':
    unittest.main()

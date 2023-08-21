
import unittest

from clean_architecture.business_entities.shot import ShotEntity
from frameworks.database.sqllite.sqllite_database import SqlLiteDatabase


class Testing(unittest.TestCase):

    def test_link_shot_to_asset(self):

        shot_id = 2
        asset_id = 4
        sql = SqlLiteDatabase()

        sql.link_shot_to_asset(asset_id, shot_id)


if __name__ == '__main__':
    unittest.main()

import unittest

from clean_architecture.business_entities.asset import AssetEntity
from clean_architecture.business_entities.shot import ShotEntity


class Testing(unittest.TestCase):

    def test_business_rules(self):

        asset_a = AssetEntity()
        asset_a.name = 'test_name_a'
        asset_a.description = 'this is a description'

        asset_b = AssetEntity()
        asset_b.name = 'test_name_a'
        asset_b.description = 'this is a description'

        asset_is_unique = asset_b.check_if_name_is_unique([asset_a])
        self.assertEqual(asset_is_unique, False)

        shot_a = ShotEntity()
        shot_a.title = 'testA'
        shot_a.cost = 100
        shot_a.budget = 200

        shot_b = ShotEntity()
        shot_b.title = 'test B'
        shot_c = ShotEntity()
        shot_c.title = 'testA'

        existing_shots = [shot_b, shot_c]
        result = shot_a.check_if_title_is_unique(existing_shots)
        self.assertEqual(result, False)

        title_is_correct = shot_a.title_sanity_check()
        self.assertTrue(title_is_correct)
        title_is_not_correct = shot_b.title_sanity_check()
        self.assertFalse(title_is_not_correct)
        is_over_budget = shot_a.is_over_budget()
        self.assertFalse(is_over_budget)


if __name__ == '__main__':
    unittest.main()

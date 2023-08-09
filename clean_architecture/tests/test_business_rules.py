import unittest

from clean_architecture.business_entities.shot import ShotEntity


class Testing(unittest.TestCase):

    def test_business_rules(self):

        shot_a = ShotEntity()
        shot_a.title = 'testA'

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


if __name__ == '__main__':
    unittest.main()

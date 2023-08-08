import unittest


class Testing(unittest.TestCase):

    def test_business_rules(self):
        from clean_architecture.business_entities.shot import ShotEntity
        shot_a = ShotEntity()
        shot_a.title = 'testA'

        shot_b = ShotEntity()
        shot_b.title = 'testB'
        shot_c = ShotEntity()
        shot_c.title = 'testA'

        existing_shots = [shot_b, shot_c]
        result = shot_a.check_if_title_is_unique(existing_shots)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
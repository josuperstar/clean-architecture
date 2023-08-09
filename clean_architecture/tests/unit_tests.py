import datetime
import unittest
from unittest import mock
from unittest.mock import Mock

from clean_architecture.business_entities.shot import ShotEntity


class Testing(unittest.TestCase):

    def test_business_rules(self):

        shot_a = ShotEntity()
        shot_a.title = 'testA'

        shot_b = ShotEntity()
        shot_b.title = 'testB'
        shot_c = ShotEntity()
        shot_c.title = 'testA'

        existing_shots = [shot_b, shot_c]
        result = shot_a.check_if_title_is_unique(existing_shots)
        self.assertEqual(result, False)

    @mock.patch('clean_architecture.use_cases.business_entity_gateway.BusinessEntityGateway.get_post_list')
    def test_use_cases(self, gateway):
        from clean_architecture.use_cases.shot_management.list_post_use_case import ListPostUseCases

        shot_a = ShotEntity()
        shot_a.id = 0
        shot_a.title = 'testA'
        shot_a.description = 'description test'
        shot_a.created = datetime.datetime.now()
        shot_list = [shot_a]

        database = Mock()
        database.get_post_list.return_value = shot_list
        use_case = ListPostUseCases(database)
        result = use_case.execute()
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
import datetime
import unittest
from copy import copy
from unittest.mock import Mock

from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.shot_management.list_post_use_case import ListPostUseCases
from clean_architecture.use_cases.shot_management.create_shot_use_case import CreateShotUseCases
from clean_architecture.use_cases.shot_management.update_shot_use_case import UpdateShotUseCases
from clean_architecture.use_cases.shot_management.delete_shot_use_case import DeleteShotUseCases



class Testing(unittest.TestCase):

    @staticmethod
    def get_shot_test():
        shot_a = ShotEntity()
        shot_a.id = 0
        shot_a.title = 'testA'
        shot_a.description = 'description test'
        shot_a.created = datetime.datetime.now()

        return shot_a

    def test_list_shot_use_case(self):
        shot_a = self.get_shot_test()
        shot_list = [shot_a]

        database = Mock()
        database.get_post_list.return_value = shot_list
        use_case = ListPostUseCases(database)
        result = use_case.execute()
        self.assertEqual(len(result), 1)

    def test_create_shot_use_case(self):
        shot_a = self.get_shot_test()
        shot_existing_one = copy(shot_a)
        shot_existing_one.title = 'titleB'
        shot_list = [shot_existing_one]

        database = Mock()
        database.get_post_list.return_value = shot_list

        use_case = CreateShotUseCases(database)
        self.assertRaises(Exception, use_case.execute)

        use_case.set_shot_info(shot_a)
        use_case.execute()


if __name__ == '__main__':
    unittest.main()

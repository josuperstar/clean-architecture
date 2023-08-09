import datetime
import unittest

from unittest.mock import Mock

from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.adapters.controllers.shot_controller import ShotController


class Testing(unittest.TestCase):

    @staticmethod
    def get_shot_test():
        shot_a = ShotEntity()
        shot_a.id = 0
        shot_a.title = 'testA'
        shot_a.description = 'description test'
        shot_a.created = datetime.datetime.now()

        return shot_a

    def test_shot_controller(self):
        shot_a = self.get_shot_test()
        shot_list = [shot_a]

        database = Mock()
        database.get_post_list.return_value = shot_list

        controller = ShotController(database)
        result = controller.get_shot_list()
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()

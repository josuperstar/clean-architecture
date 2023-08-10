import datetime
import unittest

from unittest.mock import Mock

from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.adapters.presenters.shot import ShotPresenter
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
        database.get_shot_list.return_value = shot_list

        controller = ShotController(database)

        result = controller.get_shot_list()
        self.assertEqual(len(result), 1)
        shot_presenter: ShotPresenter
        shot_presenter = result[0]
        self.assertEqual(shot_presenter.title_color, 'green')

    def test_shot_finance_controller(self):
        shot_a = self.get_shot_test()
        shot_list = [shot_a]

        database = Mock()
        database.get_shot_list.return_value = shot_list

        controller = ShotController(database)

        result = controller.get_shot_list_with_financial_data()
        self.assertEqual(len(result), 1)
        shot_presenter: ShotPresenter
        shot_presenter = result[0]
        self.assertEqual(shot_presenter.title_color, 'green')


if __name__ == '__main__':
    unittest.main()

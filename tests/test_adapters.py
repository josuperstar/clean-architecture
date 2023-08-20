import datetime
import unittest

from unittest.mock import Mock

from clean_architecture.business_entities.asset import AssetEntity
from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.adapters.presenters.shot import ShotPresenter
from clean_architecture.adapters.presenters.finance_shot import FinanceShotPresenter
from clean_architecture.adapters.controllers.shot_controller import ShotController


class Testing(unittest.TestCase):

    @staticmethod
    def get_shot_test():
        shot_a = ShotEntity()
        shot_a.id = 0
        shot_a.title = 'testA'
        shot_a.description = 'description test'
        shot_a.created = datetime.datetime.now()
        shot_a.cost = 200
        shot_a.budget = 100

        return shot_a

    @staticmethod
    def get_asset_test():
        asset_a = AssetEntity()
        asset_a.id = 0
        asset_a.name = 'test_asset_a'
        asset_a.description = 'description test'
        asset_a.created = datetime.datetime.now()
        asset_a.cost = 200

        return asset_a

    def test_shot_controller(self):
        shot_a = self.get_shot_test()
        expected_shot_list = [shot_a]

        asset_a = self.get_asset_test()

        database = Mock()
        database.get_shot_list.return_value = expected_shot_list
        database.get_asset.return_value = asset_a

        controller = ShotController(database)

        asset = controller.get_asset(0)
        self.assertEqual(asset.name, asset_a.name)

        shot_list = controller.get_shot_list()
        self.assertEqual(len(shot_list), 1)
        shot_presenter: ShotPresenter
        shot_presenter = shot_list[0]
        self.assertEqual(shot_presenter.title_color, 'green')

        shot_info = ShotEntity()
        shot_info.title = 'test_title'
        shot_info.description = 'this is a description'
        controller.create_shot(shot_info)
        shot_info.title = 'title_update'
        controller.update_shot(shot_info)
        controller.delete_shot(shot_info)

    def test_get_shot_by_asset(self):
        shot_a = self.get_shot_test()
        expected_shot_list = [shot_a]

        database = Mock()
        database.get_shots_by_asset.return_value = expected_shot_list

    def test_shot_finance_controller(self):
        shot_a = self.get_shot_test()
        shot_list = [shot_a]

        database = Mock()
        database.get_shot_list.return_value = shot_list

        controller = ShotController(database)

        result = controller.get_shot_list_with_financial_data()
        self.assertEqual(len(result), 1)
        shot_presenter: FinanceShotPresenter
        shot_presenter = result[0]
        self.assertEqual(shot_presenter.title_color, 'red')

    def test_asset_controller(self):
        asset_a = self.get_asset_test()
        expected_asset_list = [asset_a]

        database = Mock()
        database.get_asset_list.return_value = expected_asset_list
        database.get_asset.return_value = asset_a

        controller = ShotController(database)

        asset = controller.get_asset(0)
        self.assertEqual(asset.name, asset_a.name)

        assets = controller.get_asset_list()
        self.assertTrue(len(assets),1)
        self.assertEqual(assets[0].name, 'test_asset_a')


if __name__ == '__main__':
    unittest.main()

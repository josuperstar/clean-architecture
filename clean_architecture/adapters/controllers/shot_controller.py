from clean_architecture.business_entities.asset import AssetEntity
from clean_architecture.business_entities.shot import ShotEntity

from clean_architecture.adapters.presenters.asset import AssetPresenter
from clean_architecture.adapters.presenters.shot import ShotPresenter
from clean_architecture.adapters.presenters.finance_shot import FinanceShotPresenter

from clean_architecture.use_cases.shot_management.show_asset_detail_use_case import ShowAssetDetailUseCase
from clean_architecture.use_cases.asset_management.list_asset_use_case import ListAssetUseCase
from clean_architecture.use_cases.asset_management.create_asset_use_case import CreateAssetUseCase
from clean_architecture.use_cases.shot_management.list_shot_use_case import ListShotUseCase
from clean_architecture.use_cases.shot_management.create_shot_use_case import CreateShotUseCase
from clean_architecture.use_cases.shot_management.delete_shot_use_case import DeleteShotUseCase
from clean_architecture.use_cases.shot_management.update_shot_use_case import UpdateShotUseCase
from clean_architecture.use_cases.shot_management.show_shot_detail_use_case import ShowShotDetailUseCase

from clean_architecture.use_cases.boundary_objects.finance_shot_boundary import FinanceShotBoundary
from clean_architecture.use_cases.shot_finance.show_shot_detail_use_case import ShowShotFinanceDetailUseCase
from clean_architecture.use_cases.shot_finance.list_shot_finance_use_case import ListShotFianceUseCase


def asset_boundary_to_presenter(boundary):
    presenter = AssetPresenter()
    presenter.id = boundary.id
    presenter.name = boundary.name
    presenter.description = boundary.description
    presenter.name_is_correct = boundary.name_is_correct
    presenter.created = boundary.created
    return presenter


def shot_boundary_to_presenter(boundary):
    presenter = ShotPresenter()
    presenter.id = boundary.id
    presenter.title = boundary.title
    presenter.description = boundary.description
    presenter.title_size = 'h3'
    presenter.title_is_correct = boundary.title_is_correct
    presenter.created = boundary.created
    return presenter


def finance_boundary_to_presenter(boundary):
    boundary: FinanceShotBoundary
    presenter = FinanceShotPresenter()
    presenter.id = boundary.id
    presenter.title = boundary.title
    presenter.description = boundary.description
    presenter.cost = boundary.cost
    presenter.budget = boundary.budget
    presenter.is_over_budget = boundary.is_over_budget
    return presenter


class ShotController(object):

    def __init__(self, database):
        self._database = database

    def get_asset(self, asset_id):
        asset_info = AssetEntity()
        asset_info.id = asset_id
        use_case = ShowAssetDetailUseCase(self._database)
        use_case.set_asset_info(asset_info)
        asset = use_case.execute()
        presenter = asset_boundary_to_presenter(asset)
        return presenter

    def create_asset(self, asset_info):
        create_asset_use_case = CreateAssetUseCase(self._database)
        create_asset_use_case.set_asset_info(asset_info)
        create_asset_use_case.execute()

    def get_shot(self, shot_id):
        shot_info = ShotEntity()
        shot_info.id = shot_id
        use_case = ShowShotDetailUseCase(self._database)
        use_case.set_shot_info(shot_info)
        shot = use_case.execute()
        presenter = shot_boundary_to_presenter(shot)
        return presenter

    def create_shot(self, shot_info):
        create_shot_use_case = CreateShotUseCase(self._database)
        create_shot_use_case.set_shot_info(shot_info)
        create_shot_use_case.execute()

    def delete_shot(self, shot_info):
        delete_shot_use_case = DeleteShotUseCase(self._database)
        delete_shot_use_case.set_shot_info(shot_info)
        delete_shot_use_case.execute()

    def update_shot(self, shot_info):
        update_shot_use_case = UpdateShotUseCase(self._database)
        update_shot_use_case.set_shot_info(shot_info)
        update_shot_use_case.execute()

    def get_finance_shot(self, shot_id):
        shot_info = ShotEntity()
        shot_info.id = shot_id
        use_case = ShowShotFinanceDetailUseCase(self._database)
        use_case.set_shot_info(shot_info)
        shot = use_case.execute()
        presenter = finance_boundary_to_presenter(shot)
        return presenter

    def get_shot_list(self):
        list_post = ListShotUseCase(self._database)
        posts = list_post.execute()
        list_of_presenters = list()
        for post in posts:
            presenter = shot_boundary_to_presenter(post)
            list_of_presenters.append(presenter)
        return list_of_presenters

    def get_asset_list(self):
        list_asset = ListAssetUseCase(self._database)
        assets = list_asset.execute()
        list_of_presenters = list()
        for asset in assets:
            print(asset.name)
            presenter = asset_boundary_to_presenter(asset)
            list_of_presenters.append(presenter)
            print('asset name: {}'.format(presenter.name))
        return list_of_presenters

    def get_shot_list_with_financial_data(self):
        list_post = ListShotFianceUseCase(self._database)
        posts = list_post.execute()
        list_of_presenters = list()
        for post in posts:
            presenter = finance_boundary_to_presenter(post)
            list_of_presenters.append(presenter)
        return list_of_presenters


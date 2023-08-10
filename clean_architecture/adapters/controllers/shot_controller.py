from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.adapters.presenters.shot import ShotPresenter
from clean_architecture.adapters.presenters.finance_shot import FinanceShotPresenter
from clean_architecture.use_cases.shot_management.list_post_use_case import ListPostUseCases
from clean_architecture.use_cases.shot_management.show_shot_detail_use_case import ShowShotDetailUseCases
from clean_architecture.use_cases.boundary_objects.finance_shot_boundary import FinanceShotBoundary
from clean_architecture.use_cases.shot_finance.show_shot_detail_use_case import ShowShotFinanceDetailUseCases
from clean_architecture.use_cases.shot_finance.list_shot_finance_use_case import ListShotFianceUseCases


def boundary_to_presenter(boundary):
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
    return presenter


class ShotController(object):

    def __init__(self, database):
        self._database = database

    def get_shot(self, shot_id):
        shot_info = ShotEntity()
        shot_info.id = shot_id
        use_case = ShowShotDetailUseCases(self._database)
        use_case.set_shot_info(shot_info)
        shot = use_case.execute()
        presenter = boundary_to_presenter(shot)
        return presenter

    def get_finance_shot(self, shot_id):
        shot_info = ShotEntity()
        shot_info.id = shot_id
        use_case = ShowShotFinanceDetailUseCases(self._database)
        use_case.set_shot_info(shot_info)
        shot = use_case.execute()
        presenter = finance_boundary_to_presenter(shot)
        return presenter

    def get_shot_list(self):
        list_post = ListPostUseCases(self._database)
        posts = list_post.execute()
        list_of_presenters = list()
        for post in posts:
            presenter = boundary_to_presenter(post)
            list_of_presenters.append(presenter)
        return list_of_presenters

    def get_shot_list_with_financial_data(self):
        list_post = ListShotFianceUseCases(self._database)
        posts = list_post.execute()
        list_of_presenters = list()
        for post in posts:
            presenter = finance_boundary_to_presenter(post)
            list_of_presenters.append(presenter)
        return list_of_presenters


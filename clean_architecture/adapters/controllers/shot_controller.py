from clean_architecture.adapters.presenters.shot import ShotPresenter
from clean_architecture.use_cases.shot_management.list_post_use_case import ListPostUseCases


def boundary_to_presenter(boundary):
    presenter = ShotPresenter()
    presenter.id = boundary.id
    presenter.title = boundary.title
    presenter.description = boundary.description
    presenter.title_size = 'h3'
    presenter.title_is_correct = boundary.title_is_correct
    return presenter


class ShotController(object):

    def __init__(self, database):
        self._database = database

    def get_shot_list(self):
        list_post = ListPostUseCases(self._database)
        posts = list_post.execute()
        list_of_presenters = list()
        for post in posts:
            presenter = boundary_to_presenter(post)
            list_of_presenters.append(presenter)
        return list_of_presenters


from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.boundary_objects.finance_shot_boundary import FinanceShotBoundary


class ListShotFianceUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def execute(self):
        print('List shot finance use case')
        post_boundaries = list()
        posts = self._gateway.get_shot_list()
        for post in posts:
            post: ShotEntity
            post_boundary = FinanceShotBoundary()
            post_boundary.id = post.id
            post_boundary.title = post.title
            post_boundary.description = post.description
            post_boundary.cost = post.cost
            post_boundary.budget = post.budget
            post_boundary.is_over_budget = post.is_over_budget()
            post_boundaries.append(post_boundary)
        return post_boundaries

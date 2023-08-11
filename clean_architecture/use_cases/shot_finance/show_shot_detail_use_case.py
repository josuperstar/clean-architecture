from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.boundary_objects.finance_shot_boundary import FinanceShotBoundary


class ShowShotFinanceDetailUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)
        self._shot_info = None

    def set_shot_info(self, shot_info):
        self._shot_info = shot_info

    def execute(self):
        if not self._shot_info:
            raise Exception('shot info was not provided')

        shot: ShotEntity
        shot = self._gateway.get_shot(self._shot_info.id)

        post_boundary = FinanceShotBoundary()
        post_boundary.id = shot.id
        post_boundary.title = shot.title
        post_boundary.description = shot.description
        post_boundary.created = shot.created
        post_boundary.cost = shot.cost
        post_boundary.budget = shot.budget
        post_boundary.is_over_budget = shot.is_over_budget()

        return post_boundary

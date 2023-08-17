from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary


class ListShotUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def execute(self):
        print('List shot use case')
        shot_boundaries = list()
        shots = self._gateway.get_shot_list()
        for shot in shots:
            shot_entity = ShotEntity()
            shot_entity.title = shot.title
            shot_entity.description = shot.description
            is_tittle_okay = shot_entity.title_sanity_check()
            post_boundary = ShotBoundary()
            post_boundary.id = shot.id
            post_boundary.title = shot.title
            post_boundary.description = shot.description
            post_boundary.created = shot.created
            post_boundary.title_is_correct = is_tittle_okay

            shot_boundaries.append(post_boundary)
        return shot_boundaries

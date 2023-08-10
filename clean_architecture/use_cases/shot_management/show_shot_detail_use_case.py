from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.use_case import UseCases
from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary


class ShowShotDetailUseCases(UseCases):
    def __init__(self, gateway):
        super().__init__(gateway)
        self._shot_info = None

    def set_shot_info(self, shot_info):
        self._shot_info = shot_info

    def execute(self):
        if not self._shot_info:
            raise Exception('shot info was not provided')

        shot = self._gateway.get_shot(self._shot_info.id)

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

        return post_boundary

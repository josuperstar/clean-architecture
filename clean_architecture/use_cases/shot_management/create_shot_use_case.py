from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.shot_management.list_shot_use_case import ListShotUseCase


class CreateShotUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

        self._shot_info = None

    def set_shot_info(self, shot_info):
        self._shot_info = shot_info

    def execute(self):
        if not self._shot_info:
            raise Exception('shot info was not provided')

        self._shot_info: ShotBoundary
        shot_entity = ShotEntity()
        shot_entity.title = self._shot_info.title
        shot_entity.description = self._shot_info.description

        list_existing_shots = ListShotUseCase(self._gateway)
        existing_shots = list_existing_shots.execute()
        is_unique = shot_entity.check_if_title_is_unique(existing_shots)

        if not is_unique:
            raise Exception('Title is not unique')

        if not self._shot_info.title:
            raise Exception('Title is required')
        else:
            self._gateway.create_shot(self._shot_info)



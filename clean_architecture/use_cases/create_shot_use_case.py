from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.adapters.gateways.object_relational_mapping.shot import ShotModel
from clean_architecture.use_cases.use_case import UseCases
from clean_architecture.use_cases.list_post_use_case import ListPostUseCases


class CreateShotUseCases(UseCases):
    def __init__(self, gateway):
        super().__init__(gateway)

        self._shot_info = None

    def set_shot_info(self, shot_info):
        self._shot_info = shot_info

    def execute(self):
        self._shot_info: ShotModel
        shot_entity = ShotEntity()
        shot_entity.title = self._shot_info.title
        shot_entity.description = self._shot_info.description

        list_existing_shots = ListPostUseCases(self._gateway)
        existing_shots = list_existing_shots.execute()
        is_unique = shot_entity.check_if_title_is_unique(existing_shots)

        if not is_unique:
            raise Exception('Title is not unique')

        if not self._shot_info.title:
            raise Exception('Title is required')
        else:
            self._gateway.create_shot(self._shot_info)


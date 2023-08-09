from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary
from clean_architecture.use_cases.use_case import UseCases


class DeleteShotUseCases(UseCases):
    def __init__(self, gateway):
        super().__init__(gateway)
        self._shot_info = None

    def set_shot_info(self, shot_info):
        self._shot_info = shot_info

    def execute(self):
        if not self._shot_info:
            raise Exception('shot info was not provided')
        self._shot_info: ShotBoundary
        # We could add sanity check here
        self._gateway.delete_shot(self._shot_info)


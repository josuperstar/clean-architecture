from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary
from clean_architecture.use_cases.use_case import UseCase


class DeleteAssetUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)
        self._asset_info = None

    def set_asset_info(self, asset_info):
        self._asset_info = asset_info

    def execute(self):
        if not self._asset_info:
            raise Exception('Asset was not provided.')
        self._asset_info: AssetBoundary
        self._gateway.delete_asset(self._asset_info)


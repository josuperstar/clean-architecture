from clean_architecture.business_entities.asset import AssetEntity
from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.asset_management.list_asset_use_case import ListAssetUseCase


class CreateAssetUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

        self._asset_info = None

    def set_asset_info(self, asset_info):
        self._asset_info = asset_info

    def execute(self):
        if not self._asset_info:
            raise Exception('shot info was not provided')

        self._asset_info: AssetBoundary
        asset_entity = AssetEntity()
        asset_entity.name = self._asset_info.name
        asset_entity.description = self._asset_info.description

        list_existing_assets = ListAssetUseCase(self._gateway)
        existing_assets = list_existing_assets.execute()
        is_unique = asset_entity.check_if_name_is_unique(existing_assets)

        if not is_unique:
            raise Exception('Name is not unique')

        if not self._asset_info.name:
            raise Exception('Name is required')
        else:
            self._gateway.create_asset(self._asset_info)



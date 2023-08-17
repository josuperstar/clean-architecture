from clean_architecture.business_entities.asset import AssetEntity
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary


class ShowAssetDetailUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)
        self._asset_info = None

    def set_asset_info(self, asset_info):
        self._asset_info = asset_info

    def execute(self):
        if not self._asset_info:
            raise Exception('shot info was not provided')

        asset = self._gateway.get_asset(self._asset_info.id)

        asset_entity = AssetEntity()
        asset_entity.name = asset.name
        asset_entity.description = asset.description
        is_tittle_okay = asset_entity.name_sanity_check()
        asset_boundary = AssetBoundary()
        asset_boundary.id = asset.id
        asset_boundary.name = asset.name
        asset_boundary.description = asset.description
        asset_boundary.created = asset.created
        asset_boundary.title_is_correct = is_tittle_okay

        return asset_boundary

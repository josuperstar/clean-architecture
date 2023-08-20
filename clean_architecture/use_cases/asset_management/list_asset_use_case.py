from clean_architecture.business_entities.asset import AssetEntity
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary


class ListAssetUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def execute(self):
        print('List asset use case')
        asset_boundaries = list()
        assets = self._gateway.get_asset_list()
        for asset in assets:
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

            asset_boundaries.append(asset_boundary)
        return asset_boundaries

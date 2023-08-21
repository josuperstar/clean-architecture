from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.use_case import UseCase
from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary
from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary
from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway

class ShowShotDetailUseCase(UseCase):
    def __init__(self, gateway):
        super().__init__(gateway)
        self._shot_info = None

    def set_shot_info(self, shot_info):
        self._shot_info = shot_info

    def execute(self):
        if not self._shot_info:
            raise Exception('shot info was not provided')
        self._gateway: BusinessEntityGateway
        shot = self._gateway.get_shot(self._shot_info.id)
        assets = self._gateway.get_assets_by_shot(shot.id)
        asset_boundaries = list()
        for asset in assets:
            asset_boundary = AssetBoundary()
            asset_boundary.id = asset.id
            asset_boundary.name = asset.name
            asset_boundary.description = asset.description
            asset_boundary.created = asset.created
            asset_boundary.title_is_correct = True
            asset_boundaries.append(asset_boundary)

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
        post_boundary.assets = asset_boundaries

        return post_boundary

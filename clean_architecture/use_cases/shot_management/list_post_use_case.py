from clean_architecture.business_entities.shot import ShotEntity
from clean_architecture.use_cases.use_case import UseCases
from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary


class ListPostUseCases(UseCases):
    def __init__(self, gateway):
        super().__init__(gateway)

    def execute(self):
        print('List post use case')
        post_boundaries = list()
        posts = self._gateway.get_post_list()
        for post in posts:
            shot_entity = ShotEntity()
            shot_entity.title = post.title
            shot_entity.description = post.description
            is_tittle_okay = shot_entity.title_sanity_check()
            post_boundary = ShotBoundary()
            post_boundary.id = post.id
            post_boundary.title = post.title
            post_boundary.description = post.description
            post_boundary.created = post.created
            post_boundary.title_is_correct = is_tittle_okay

            post_boundaries.append(post_boundary)
        return post_boundaries

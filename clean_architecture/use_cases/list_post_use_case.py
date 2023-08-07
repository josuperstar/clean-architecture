from clean_architecture.use_cases.use_case import UseCases
from clean_architecture.use_cases.post_boundary import PostBoundary


class ListPostUseCases(UseCases):
    def __init__(self, gateway):
        super().__init__(gateway)

    def execute(self):
        print('List post use case')
        post_boundaries = list()
        posts = self._gateway.get_post_list()
        for post in posts:
            post_boundary = PostBoundary()
            post_boundary.id = post.id
            post_boundary.title = post.title
            post_boundary.content = post.content
            post_boundary.created = post.created
            post_boundaries.append(post_boundary)
        return post_boundaries

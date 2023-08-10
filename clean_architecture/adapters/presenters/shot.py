from clean_architecture.use_cases.boundary_objects.shot_boundary import ShotBoundary


class ShotPresenter(ShotBoundary):

    def __init__(self):
        super().__init__()
        self.title_size = 'big'

    @property
    def title_color(self):
        print('presenter title is correct {}'.format(self.title_is_correct))
        if not self.title_is_correct:
            return 'red'
        return 'green'


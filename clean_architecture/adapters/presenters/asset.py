from clean_architecture.use_cases.boundary_objects.asset_boundary import AssetBoundary


class AssetPresenter(AssetBoundary):

    def __init__(self):
        super().__init__()

    @property
    def name_color(self):
        print('presenter name is correct {}'.format(self.name_is_correct))
        if not self.name_is_correct:
            return 'red'
        return 'green'


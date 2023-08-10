from clean_architecture.use_cases.boundary_objects.finance_shot_boundary import FinanceShotBoundary


class FinanceShotPresenter(FinanceShotBoundary):

    def __init__(self):
        super().__init__()
        self.title_size = 'big'

    @property
    def title_color(self):
        return 'blue'


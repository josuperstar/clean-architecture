from clean_architecture.use_cases.boundary_objects.finance_shot_boundary import FinanceShotBoundary


class FinanceShotPresenter(FinanceShotBoundary):

    def __init__(self):
        super().__init__()
        self.title_size = 'big'

    @property
    def title_color(self):
        if self.is_over_budget:
            return 'red'
        return 'blue'

    def __str__(self):
        return "{} {} {} {} {}".format(
            self.id,
            self.title,
            self.created,
            self.cost,
            self.budget,
            self.is_over_budget
        )
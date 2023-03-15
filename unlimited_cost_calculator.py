class UnlimitedCostCalculator:

    def __init__(self):
        self.total_cost: float

    def excecute(self):
        self.total_cost = 54.90

    def __str__(self):
        return f"{self.total_cost}"

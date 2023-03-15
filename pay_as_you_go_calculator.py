class PayAsYouGoCalculator:

    def __init__(self, call_minutes, sms_count):
        self.call_minutes = call_minutes
        self.sms_count = sms_count
        self.total_cost: float

    def excecute(self):
        self.call_cost = 0.12 * self.call_minutes
        self.sms_cost = 0.12 * self.sms_count
        self.total_cost = self.call_cost + self.sms_cost

    def __str__(self):
        return f"{self.total_cost}"

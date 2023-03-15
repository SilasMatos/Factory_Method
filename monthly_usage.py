from pay_as_you_go_calculator import PayAsYouGoCalculator
from unlimited_cost_calculator import UnlimitedCostCalculator


class MonthlyUsage:

    def Pay_Calculator(self, call_minutes, sms_count):
        return PayAsYouGoCalculator(call_minutes, sms_count)

    def Unlimited_Calculator(self):
        return UnlimitedCostCalculator()

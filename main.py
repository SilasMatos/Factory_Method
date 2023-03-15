from monthly_usage import MonthlyUsage

monthly = MonthlyUsage()
pay_calculator = monthly.Pay_Calculator(1, 2)
unlimited_calculator = monthly.Unlimited_Calculator()
pay_calculator.excecute()
unlimited_calculator.excecute()
print(pay_calculator)
print(unlimited_calculator)

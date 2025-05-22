monthlyIncome = int(input("Enter your monthly income: "))
totalExpenses = int(input("Enter your total monthly expenses: "))
monthlySavings = monthlyIncome - totalExpenses
print(f"Your monthly savings are ${monthlySavings}")

# Calculating projected savings after a year
projectedSavings = (monthlySavings * 12 ) + (monthlySavings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${projectedSavings}.")
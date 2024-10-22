# Example for interest rate
interest_rate = 6  # Example interest rate

# Calculating years using the rule of 72
years_to_double = 72 / interest_rate

# Result
print("At " + str(interest_rate) + "% interest rate, your savings account will be worth double in " + str(format(years_to_double, ".1f")) + " years")

# Author: Rodolfo
# Date: October 28th
# This script is a progress tracker with a 75% milestone

# Bank balance, savings goal, and weekly savings with a treat at the 75% mark
balance = float(input("Starting balance: "))
goal = float(input("Savings goal: "))
weekly_savings = float(input("Weekly savings: "))
treat_given = False

# saving goal
while balance < goal:
    balance += weekly_savings
    print(f"Balance increased to ${balance:.2f}")

    # 75% progress message with one-time treat
    if balance >= goal * 0.75 and not treat_given:
        treat = 10  # Amount for the treat
        balance -= treat
        print(f"So close! After treating myself, my balance is up to ${balance:.2f}")
        treat_given = True  # The treat is only given once

# Results
print(f"Goal met! Final balance: ${balance:.2f}")
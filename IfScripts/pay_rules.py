
# Author: Rodolfo Lopez
# Date: October 25th
# This script calculates gross pay, including overtime pay if it applies. 

# Input variables: hourly pay rate and hours worked
pay_rate = float(input("Enter your pay rate per hour: "))
hours_worked = float(input("Enter the number of hours worked: "))

# If hours worked exceed 40, calculate overtime pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate  # first 40 hours
    overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)  # Overtime pay 
    gross_pay = regular_pay + overtime_pay  # Total gross pay including overtime
else:
    gross_pay = hours_worked * pay_rate  # Regular pay with no overtime

# Calculated gross pay, formatted to two decimal places
print(f"Gross pay: ${gross_pay:.2f}")
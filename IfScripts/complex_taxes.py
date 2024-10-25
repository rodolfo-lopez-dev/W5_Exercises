# Author: Rodolfo
# Date: October 25th
# This script calculates taxs based on the annual gross income and filing status.

# pay rate and hours worked to calculate weekly gross pay
pay_rate = float(input("Enter your pay rate per hour: "))
hours_worked = float(input("Enter the number of hours worked: "))

# Calculate weekly gross pay, including overtime if hours exceed 40
if hours_worked > 40:
    regular_pay = 40 * pay_rate  
    overtime_pay = (hours_worked - 40) * (pay_rate * 1.5) 
    weekly_gross_pay = regular_pay + overtime_pay
else:
    weekly_gross_pay = hours_worked * pay_rate 

# Estimate annual gross income based of a 52 week year
annual_gross_income = weekly_gross_pay * 52

# Looking for filing status (single or joint)
filing_status = input("Enter your filing status (single/joint): ")

# Determine the tax rate based on filing status and annual income
if filing_status == 'single':
    if annual_gross_income <= 9875:
        tax_rate = 0.10
    elif annual_gross_income <= 40125:
        tax_rate = 0.12
    elif annual_gross_income <= 85525:
        tax_rate = 0.22
    elif annual_gross_income <= 163300:
        tax_rate = 0.24
    else:
        tax_rate = 0.32
elif filing_status == 'joint':
    if annual_gross_income <= 19750:
        tax_rate = 0.10
    elif annual_gross_income <= 80250:
        tax_rate = 0.12
    elif annual_gross_income <= 171050:
        tax_rate = 0.22
    elif annual_gross_income <= 326600:
        tax_rate = 0.24
    else:
        tax_rate = 0.32

# Tax withholding for the weekly pay
weekly_tax = weekly_gross_pay * tax_rate

# Net weekly pay after taxes
net_weekly_pay = weekly_gross_pay - weekly_tax

# Results
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross_pay:.2f}.")
print(f"Your filing status is {filing_status}.")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}.")
print(f"Your net weekly pay is ${net_weekly_pay:.2f}.")
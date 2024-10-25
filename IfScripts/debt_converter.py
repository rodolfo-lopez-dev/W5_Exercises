# Author: Rodolfo 
# Date: October 25th
# This script translates department code into names


# dept code from user input to int 

dept_code = int(input("Enter the department code: ")) 

# dept_code and corresponding dept name

if dept_code == 1:
    print("Department: Marketing")
elif dept_code == 5:
    print("Department: Human Resources")
elif dept_code == 10:
    print("Department: Accounting")
elif dept_code == 12:
    print("Department: Legal")
elif dept_code == 18:
    print("Department: IT")
elif dept_code == 20:
    print("Department: Customer Relations")

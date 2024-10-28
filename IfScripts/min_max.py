# Author: Rodolfo
# Date: October 28th
# This script finds and displays the smallest and largest of three numbers.

# a,b and c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Assign a to the smallest and largest
smallest = a
largest = a

# Check if b is smaller or larger than the current smallest and largest
if b < smallest:
    smallest = b
else:
    smallest = smallest  # Keep the same value if b ≥ a

if b > largest:
    largest = b
else:
    largest = largest  # Change only if b is larger.

# Check if c is smaller or larger than the current smallest and largest
if c < smallest:
    smallest = c
else:
    smallest = smallest  # No change if c ≥
if c > largest:
    largest = c
else:
    largest = largest  # No change if c ≤

#  results
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
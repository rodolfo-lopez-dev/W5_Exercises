x = 100
y = 20 

# first instance

if x / y == 5: 
    print("x divided by y is 5")
    x = 1 
else: 
    print("Are the variable set up correctly?")

# second instance 

if x * y == y:
    print("now x times y is y")
    x = 10 
else:
    print("Whoops, x equals", x)

# third instance 

if x < y:
    print("x is less than y")
    x *= 2 # we're doubling x 
else:
    print("uh oh, x is not less than y")

if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

print(f"The final value of x is {x} and the final value of y is {y}")
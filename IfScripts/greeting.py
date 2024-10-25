# Author: Rodolfo 
# Date: October 25th 
# This scripts shows greetings depending on time of day 

# def a variable that contains current hours (0-23)

current_hour = int(input("Enter the current hour (0-23): "))

# associate appropriate greeting
if current_hour < 10:
    print ("Good morning!")
elif 10 <= current_hour < 17:
    print ("Good day!")
elif 17 <= current_hour < 23:
    print("Good evening!")
else:
    print("What are you doing up so late??")
# how to convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2) 

print(fahrenheit_to_celsius(98.6))

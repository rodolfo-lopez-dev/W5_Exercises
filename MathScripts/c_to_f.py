# how to convert celsius to fahrenheit 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)

print(celsius_to_fahrenheit(35))
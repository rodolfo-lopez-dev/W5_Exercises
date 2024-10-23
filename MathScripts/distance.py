import math

def calculate_distance(x1, y1, x2, y2):
    x_dif = x2 - x1 
    y_dif = y2 - y1
    distance = math.sqrt((x_dif * x_dif) + (y_dif * y_dif))
    return distance
print(calculate_distance(0, 0, 3, 4))
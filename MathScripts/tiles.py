import math

def calculate_tiles(lenght, width):
    area = lenght * width 
    tiles_needed = math.ceil(area / 12)
    total_boxes = math.ceil(tiles_needed * 1.1)
    return total_boxes
print(calculate_tiles(6, 9))
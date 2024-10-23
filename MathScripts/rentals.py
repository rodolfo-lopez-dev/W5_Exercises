import math

def calculate_rentals(people, cost_per_day):
    vans_needed = math.ceil(people / 15)  # Each van holds 15 people
    total_cost = vans_needed * cost_per_day
    cost_per_person = round(total_cost / people, 2)
    return vans_needed, total_cost, cost_per_person

print(calculate_rentals(38, 250))  # Test with 38 people and $250 per van
# creating a dictionary 
address_entry = {
    "name": "Rodolfo Lopez",
    "address": "321 W 12 St",
    "city": "Chicago",
    "state": "Illinois",
    "zip": "60629"
}

# print the address as properly format for mail
print("\nFormatted address:")
print(f"{address_entry['name']}\n{address_entry['address']}\n{address_entry['city']}, {address_entry['state']} {address_entry['zip']}")

# remove 'name' 
address_entry.pop('name')

# add 'full_name' 
address_entry["full_name"] = ("Rodolfo", "Lopez")

# adding honorific by using .update()
address_entry.update({"honorific": "Mr"})

# print again 
print("\nFormatted address:")
print(f"{address_entry['honorific']} {address_entry['full_name'][0]} {address_entry['full_name'][1]}")
print(f"{address_entry['address']}")
print(f"{address_entry['city']}, {address_entry['state']} {address_entry['zip']}")

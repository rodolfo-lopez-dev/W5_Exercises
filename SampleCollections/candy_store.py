# creating tuple for candy that comes in fruit flavors
candy_type = ('Sour Worms', 'Jelly Beans', 'Lollipops')

# type of flavors
candy_flavors = ('Watermelon', 'Strawberry', 'Grape')

# using set to stor candy combos and using assigning simple combos

candy_combo = set()
candy_combo.add(candy_type[0] + ' - ' + candy_flavors[0])
candy_combo.add(candy_type[1] + ' - ' + candy_flavors[1])
candy_combo.add(candy_type[2] + ' - ' + candy_flavors[2])

print("Today's candy options include:")
print(candy_combo)

# printing the outcome multiple times will lead to different combinations of candy's and flavors
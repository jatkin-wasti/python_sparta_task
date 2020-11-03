# Collections in python
# Lists?
# Lists are a MUTABLE collection of items that can be indexed and split
# Being mutable means we can add, remove, change an item in the list
# Lists can hold multiple data types!
# Syntax of a list ["yoghurt", "apple", "milk"]
# Indexing starts as 0 (as it should)
# Can use negative indexing e.g. list[-1] for our previous list will return milk

# lets create a list
# shopping_list = ["apple", "milk", "bread"]
# print(shopping_list)  # This will print the entire list
# print(type(shopping_list))  # This will print the type of the variable which in this case is a list
#
# # look at indexing in the list of items
# print(shopping_list[1])  # This will print milk as its the second item in the list and indexes start at 0
# print(shopping_list[2])  # This will print bread as its the third item in the list and indexes start at 0
# print(shopping_list[1:3])  # This will print the second and third item in the list as the : is exclusive
# # of the number after it
# print(shopping_list[::-1])  # This will print the list in reverse as the syntax for getting items in a list
# is [start_index:end_index:step_increment] so if the first two are left blank it assumes it wants from the
# start to the end

# Managing a list
# add an item to this list
# shopping_list.append("eggs")  # append method adds an item at the end of the list
# print(shopping_list)
#
# # how can we remove an item from a list
# shopping_list.remove("apple")
# print(shopping_list)
#
# # how can we remove the last item added to the list
# print(shopping_list.pop())  # popping an item also returns the value so we can use this in a print or call
# print(shopping_list)
#
# # how can I replace an item in my list?
# shopping_list[1] = "potato"
# print(shopping_list)
#
# # can we have mixed data types in a list?
# shopping_list.append(74)  # attempting to add an int to the list of strings
# print(shopping_list)  # This runs and shows that the list can hold different data types

# Task: Create a mixed data type list containing 7 items
# display the type of the data stored in the list
# add, delete, replace, pop the list
# use indexing to return the list in reverse order
# mixed_list = ["Sunny", "Windy", "Rainy", "Stormy", 27, 13, -5]  # Creates a list with weather and temperature
# print(type(mixed_list[0]))  # shows the type of the item in position 0
# print(type(mixed_list[6]))  # shows the type of the item in position 6
# mixed_list.pop()  # removes the last item from the list, in this case it removes the -5 temperature
# mixed_list.append(36)  # this adds a temperature of 36 to the list
# mixed_list.remove(27)  # this removes the temperature recording of 27 from the list
# mixed_list[0] = "Clear skies"  # this changes the "Sunny" item to "Clear skies"
# print(mixed_list)  # this prints the now changed list
# print(mixed_list[::-1])  # this prints the list in reverse order

# Tuples are IMMUTABLE - CAN'T BE CHANGED
# Use cases: fixed data e.g NI number, NHS number, date of birth, place of birth, blood type
# Syntax of a tuple is ("paracetamol", "eggs", "supermalt")

# Lets create a tuple
short_list = ("paracetamol", "eggs", "supermalt")
print(short_list)  # This prints the tuple
print(type(short_list))  # This shows the data type is a tuple
# short_list[1] = "fruit"  # This will throw a TypeError as tuples do not support item assignment
# If you need to change something in a tuple, you can convert the tuple into a list, change the list, and
# then convert it back to a tuple
print(short_list[::-1])  # This prints a reversed version of the tuple
print(short_list[0])  # This prints the first index in the tuple
print(short_list[1])  # This prints the second index in the tuple
print(short_list[2])  # This prints the third index in the tuple

# What are sets?
# There is no indexing in sets therefore
# Sets are UNORDERED
# Syntax for sets is {"value1", "value2", "value3"}
# Use cases: Data that needs to be stored for long periods of time but there is low demand to access it
# Also useful for random sets of data e.g. lottery numbers

#
car_parts = {"wheels", "doors", "engine", "radio", "steering wheel"}
print(car_parts)  # This does not return the values in the same order that it was input

# managing data with sets
car_parts.add("seatbelts")  # Can add items with add()
print(car_parts)
car_parts.remove("wheels")  # Can remove items with remove()
print(car_parts)

# Look up frozen sets as a task

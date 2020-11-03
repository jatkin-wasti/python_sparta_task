# What is a dictionary
# Dictionaries are another way of managing collected data but more dynamically
# Uses a key value pairs to store the data instead of indexes
# Syntax of a dictionary is {key1:value1, key2:value2} e.g. {"name": "James, "code": 007}
# What type of data can we store in a dictionary? Any.

# Lets create a dictionary
devops_students = {
    "key": "value",
    "name": "Jamie",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["Variables", "Data Types", "Operators", "Concatenation"]
}
print(type(devops_students))  # This shows that it is a dictionary
print(devops_students)  # This prints out the entire dictionary
print(devops_students["name"])  # This prints out just the value corresponding to the "name" key
print(devops_students.keys())  # This prints out all of the keys stored in the dictionary
print(devops_students.values())  # This prints out all of the values stored in the dictionary
# This prints out the entire list stored in the "completed_lesson_names" key
print(devops_students["completed_lesson_names"])
print(devops_students["completed_lesson_names"][1])

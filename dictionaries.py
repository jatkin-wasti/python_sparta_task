# # What is a dictionary
# # Dictionaries are another way of managing collected data but more dynamically
# # Uses a key value pairs to store the data instead of indexes
# # Syntax of a dictionary is {key1:value1, key2:value2} e.g. {"name": "James, "code": 007}
# # What type of data can we store in a dictionary? Any.
#
# # Lets create a dictionary
# devops_students = {
#     "key": "value",
#     "name": "Jamie",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lesson_names": ["Variables", "Data Types", "Operators", "Concatenation"]
# }
# print(type(devops_students))  # This shows that it is a dictionary
# print(devops_students)  # This prints out the entire dictionary
# print(devops_students["name"])  # This prints out just the value corresponding to the "name" key
# print(devops_students.keys())  # This prints out all of the keys stored in the dictionary
# print(devops_students.values())  # This prints out all of the values stored in the dictionary
# # This prints out the entire list stored in the "completed_lesson_names" key
# print(devops_students["completed_lesson_names"])
# # This accesses the second item in the list stored in the "completed_lesson_names" key
# print(devops_students["completed_lesson_names"][1])
# # This accesses the second and third item in the list stored in the "completed_lesson_names" key
# print(devops_students["completed_lesson_names"][1:3])
# # This will iterate through the values and show what data types they are
# for _ in devops_students.values():
#     print(type(_))
#
# # How can I change the value of a specific key
# devops_students["completed_lessons"] = 3
# print(devops_students["completed_lessons"])
# print(devops_students.items())  # This returns each key value pair as its own item as a dictionary items type

# Task
# Create a dictionary to store user details
# All the details that you utilised in the last task: name, DOB, Address, Course, Grades
# Utilise methods to add, remove, replace, display the types of items
# Create a list of hobbies of at least 3 items
# Display data in reverse order of hobby list
# First we create the dictionary with general information, including an incorrect date of birth
trainee_dictionary = {
    "name": "Jamie Atkin-Wasti",
    "date_of_birth": "16/10/19997",
    "address": "54a Highfield Avenue NW9 0PY",
    "course": "DevOps",
    "grades": [80, 68]
}
# Then we add a list of hobbies to the dictionary under the "hobbies" key
trainee_dictionary["hobbies"] = ["Bouldering", "Dungeons and Dragons", "Baking"]
# We can delete a key value pair with the del method which in this case deletes the course key value pair
del trainee_dictionary["course"]
# We can correct the date of birth by selecting the key and assigning it the corrected value
trainee_dictionary["date_of_birth"] = "16/10/1997"
# Looping through all of the values stored in the trainee_dictionary and printing out their types
# Remember that we got rid of "course" and added "hobbies" so there will be one fewer string and one more list!
for _ in trainee_dictionary.values():
    print(type(_))
# Finally we print out the hobbies in reverse order
print(trainee_dictionary["hobbies"][::-1])

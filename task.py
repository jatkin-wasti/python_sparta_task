# The capitalize() function ensures that the string starts with a capital letter even if the user has input
# in all lowercase
# Receiving the user input for their first name and stores it as a string in the first_name variable
first_name = input("Please enter your first name:  ").capitalize()
# Receiving the user input for their middle name and stores it as a string in the middle_name
# variable and since not everyone has a middle name it allows them to leave this variable as an empty string
middle_name = input("If you have a middle name please enter it here, if not please press Enter:  ").capitalize()
# Receiving the user input for their last name and stores it as a string in the last_name variable
last_name = input("Please enter your last name:  ").capitalize()
# Receiving the user input for their NI number and stores it as a string in the ni_num variable
# All letters in an NI number are capitals so we make sure that this is the case with the upper function
ni_num = input("Please enter your National Insurance number:  ").upper()

# Receiving the user input for their house number and storing it as a string in the house_number variable
house_number = int(input("Please enter your house number:  "))  # No need to modify this input
# Receiving the user input for the first line of their address and storing it as a string in the
# house_number variable, ensuring that the first letter of each word in the address is capitalised with title
first_line_address = input("Please enter the first line of your address:  ").title()
# Receiving the user input for their post code and storing it as a string in the post_code variable
post_code = input("Please enter your Post Code:  ").upper()  # Post codes are generally all upper case

# Receiving the user input for their course and storing it as a string in the course variable
course = input("Please enter the course you have applied to:  ").capitalize()
# Receiving the user input for their education and storing it as a string in the recent_education variable
recent_education = input("Please enter your most recent form of education:  ").capitalize()

# Print statements that display the information received using fstrings
print(f"Welcome to Sparta, {first_name} {middle_name} {last_name}!")
print(f"Your National Insurance number is: {ni_num}")
print(f"To confirm, your address is as shown:\n"
      f"{str(house_number)} {first_line_address}\n"
      f"{post_code}")
print(f"You are enrolling on the {course} course, and your most recent form of education "
      f"was {recent_education}.")

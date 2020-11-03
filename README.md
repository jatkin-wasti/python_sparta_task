# Task: Take user input details for a new Spartan
## Solution
We use the input() function to obtain a users 
input. 
```
name = input("Please enter your name:  ")
```
We store this information in a series of 
logically named variables. Where appropriate we 
use the capitalise() function to make sure that 
strings begin with a capital letter. 
```
string_here.capitalize()
```
In certain 
cases, such as with an NI number, we instead use 
the upper() function to make sure the entire 
string is capitalised. 
```
string_here.upper()
```
We then use f strings to
concatenate a message with the values we've been 
given by the user.
```
print(f"This is a string that includes data 
stored in {variable}")
```
## Acceptance Criteria
- Take trainee date from user
- Ensure the first letter of each string is capital
- Use casting to change data type
- Ensure to take the appropriate data type in

## DoD (Definition of Done)
- Must have 3 commits
- Must be in new github repo 
- All acceptance criteria achieved
# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    age = input('Please enter your age: ')

    voting_age = 18

    voters_age = int(age)

    if voters_age >= 0:

        if voters_age >= voting_age:
            print("You are eligible to vote.")
        else: 
            print(f"Sorry, you are not eligible to vote. You must be at least {voting_age} years old to vote.")
    else: 
        print("Age cannot be negative. Please enter a valid age")

check_voting_eligibility()
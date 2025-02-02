# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month_input = input('Enter a month of the year (Jan - Dec): ')
    day_input = input('Enter the day of the month: ')

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    day_input = int(day_input)

    if month_input not in months: 
        print('Invalid month entered. Please enter a valid month abbreviated to the first three letters of the month name.')
    if day_input <1 or day_input >31: 
        print('Invalid day input. Please enter a number from 1-31.')
    
    if (month_input == 'Dec' and day_input >= 21) or (month_input == 'Jan') or (month_input == 'Feb') or (month_input == 'Mar' and day_input < 21):
        season = 'Winter'
    elif (month_input == 'Mar' and day_input >= 21) or (month_input == 'Apr') or (month_input == 'May') or (month_input == 'Jun' and day_input < 21):
        season = 'Spring'
    elif (month_input == 'Jun' and day_input >= 21) or (month_input == 'Jul') or (month_input == 'Aug') or (month_input == 'Sept' and day_input < 21):
        season = 'Summer'
    elif (month_input == 'Sept' and day_input >= 21) or (month_input == 'Oct') or (month_input == 'Nov') or (month_input == 'Dec' and day_input < 21):
        season = 'Spring'
    print(f'{month_input} {day_input} is in {season}.')


determine_season()
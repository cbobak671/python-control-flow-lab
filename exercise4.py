# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():

    is_it_cold = input("Is it cold (yes/no): ").lower()

    is_it_raining = input("Is it raining (yes/no)?: ").lower()

    if is_it_cold == 'yes' and is_it_raining == 'yes':
        print('Wear a waterproof coat.')
    elif is_it_cold == 'yes' and is_it_raining == 'no':
        print('Wear a warm coat.')
    elif is_it_cold == 'no' and is_it_raining == 'yes':
        print('Carry an umbrella.')
    elif is_it_cold == 'no' and is_it_raining == 'no':
        print('Wear light clothing.')

weather_advice()
"""
Change
Ella Chakravarty

Converts number of cents into the fewest number of US coins that amount.
"""

#Formatting the input
total_cents = int(input('Please enter a number of cents:'))

#Assigning values to variables
quarter = 25
dime = 10
nickel = 5
penny = 1

#Expressions for number of coins
quarters = total_cents // quarter
dimes = (total_cents - (quarter * quarters)) // dime
nickels = (total_cents - (quarters * quarter) - (dime * dimes)) // nickel
pennies = (total_cents - (quarter * quarters) - (dime *dimes) - (nickel * nickels))// penny

#Formatting the output
print('Coins:', quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels,', pennies, 'pennies')
"""
Pizza Party
Ella Chakravarty

Calculate the following for a pizza party: area of a pizza, area per person, total slices, and slices per person, based on information from the user. 
"""

#Assigning values from input to variables
num_people = int(input('Please enter the number of people attending the party:'))
num_pizzas = int(input('Please enter the number of pizzas purchased for the party:'))
diameter_pizzas = int(input('Please enter the diameter of the pizzas:'))
num_slices_per_pizza = int(input('Please enter the number of slices per pizza:'))
radius_pizzas = (diameter_pizzas / 2)

#Expressions for output
total_area = round(3.14 * (radius_pizzas) * (radius_pizzas) * num_pizzas, 2)
area_per_person = round((total_area / num_people), 2)
total_slices = (num_slices_per_pizza * num_pizzas)
slices_per_person = (total_slices / num_people)

#Formatting output
print('Total pizza area:', total_area, 'square inches')
print('Total number of slices:', total_slices)
print('Pizza area per person:', area_per_person, 'square inches')
print(f'Slices per person: {slices_per_person:.2f}')
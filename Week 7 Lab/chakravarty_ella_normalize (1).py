"""
Normalize
Ella Chakravarty

Program adjusts input values by dividing all inputs by largest value
"""

num_values = int(input('Please enter the number of floating point values:'))
float_values = []
for i in range(num_values):
    float_values.append(float(input('Please enter a floating-poit value:')))
    

print('Normalized Floating-Point Values:')
for norm in range(num_values):
    print(f'{float_values[norm]/max(float_values):.2f}')
    
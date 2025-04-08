"""
Triangle Area
Ella Chakravarty

Calculate the area of a triangle using input from user. 
"""

#Assigning values from input to variables
base = int(input('Enter the length of the base:'))
height = int(input('Enter the height:'))

#Expression for area of a triangle using floor division operator
result = (base * height // 2)

#Formatting the output
print('The area of the triangle is ', end='')
print(result, 'm^2')
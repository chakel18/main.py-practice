"""
Modules
Ella Chakravarty

Calculate the volume of a sphere and calculate the factorial of a randomly generated number between 1 and 10. 
"""

#Formatting input
radius = int(input('Please enter the radius of the sphere:'))
import math
import random

#Expression for volume of a sphere
volume = (4/3) * math.pi * radius ** 3

#Expression for factorial of randomly generated number (1-10)
number = random.randint(1,10)
factorial = math.factorial(number)

#Formatting the output
print('The volume of a sphere with radius of', radius, f'is {volume: .2f}')
print('The factoial of', number, 'is', factorial)
"""
Calories
Ella Chakravarty

Estimate the average calories burned for a person when exercising.
"""

#Assign values to variables and formatting the input
age = int(input('Please enter your age:'))
weight = int(input('Please enter your weight in pounds:'))
heart_rate = int(input('Please enter your heart rate in beats per minute:'))
workout_duration = int(input('Please enter the length of your workout in minutes:'))

#Expression of calories burned when exercising
calories = ((age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * workout_duration) / 8.368

#Formatting the Output
print(f'Calories burned: {calories: .2f}')

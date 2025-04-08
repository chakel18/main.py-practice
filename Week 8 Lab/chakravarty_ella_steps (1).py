"""
Steps
Ella Chakravarty

Program calculates number of steps walked from distance in feet. 

"""

#define function feet_to_steps and expression for conversion
def feet_to_steps(feet_walked):
    return int(feet_walked / 2.5)

#Prompt user for input
feet_walked = float(input("Please enter the distance traveled in feet:"))

#Format ouput
steps = feet_to_steps(feet_walked)
print(f"{steps} steps")

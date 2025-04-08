"""
Speeding
Ella Chakravarty

Calculate speeding ticket amount based on speed limit and driving speed. 
"""
#Formatting the input
limit = int(input("Please enter the speed limit for the road:"))
speed = int(input("Please enter the vehicle's recorded speed:"))

#Writing the conditions 
if speed <= (limit - 10):
    print("The speeding fine is $50.")
elif speed < (limit - 9):
    print("There is no fine.")
elif (limit + 6) <= speed <= (limit + 20):
    print("The speeding fine is $75.")
elif (limit + 21) <= speed <= (limit + 40):
    print("The speeding fine is $150.")
elif (limit + 40) <= speed:
    print("The speeding fine is $300.")
else:
    print("There is no fine.")
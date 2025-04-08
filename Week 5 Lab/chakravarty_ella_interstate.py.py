"""
Interstate
Ella Chakravarty

Indicate whether the highway number is primary, auxiliary, or invalid highway number. Also indicate what direction the highway runs.
"""

#Formatting the input
number = int(input("Please enter an interstate number:"))

#Writing conditions
if 1 <= number <= 99:
    if number % 2 == 0:
        print("I-", number, end="")
        print(" is primary, going east/west.")
    else:
        print("I-", number, "is primary, going north/south.")
elif number % 100 == 00:
    print(number, " is not a valid interstate highway number.")
elif 100 <= number <= 999:
    if number % 2 == 0:
        print("I-", number, "is auxillary,",end="")
        print(f" serving I - {number % 100},", end="")
        print(" going east/west.")
    else:
        print("I-", number, "is auxillary,",end="")
        print(f" serving I - {number % 100},", end="")
        print(" going north/south.")




    


    
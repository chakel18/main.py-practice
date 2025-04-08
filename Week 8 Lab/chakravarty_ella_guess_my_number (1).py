"""
Guess My Number
Ella Chakravarty

Program generates random number that user must guess within 10 attempts. 
"""
#Import appropriate module
import random

#define number_guessing_game, print user instruction
def number_guessing_game():
    random_number = random.randint(1,100)
    print("I have generated a number between 1 and 100. You will have 10 attempts to guess that number.")

#Gather input, format output based on condition
    for attempt in range (1,11):
        guess = int(input(f'Guess {attempt}:'))

#Nested loop
        if guess > random_number:
            print("Your guess is greater than my random number. Try again.")
        elif guess < random_number:
            print("Your guess is less than my random number. Try again.")
        else:
            print("You correctly guessed my random number!")
            break
    else:
        print(f"Sorry! You've run out of attemps. The correct number was {random_number}.")

#call function to run game automatically after script executed
number_guessing_game()

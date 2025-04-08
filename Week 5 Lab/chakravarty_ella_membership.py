"""
Membership
Ella Chakravarty

Determine whether a given character is a vowel, consonant, digit, or punctuation.
"""
#Lists of character type
vowels = ["a", "e", "i", "o", "u"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
punctuation = [",",";",".","?","!"]

#Formatting input
character = input('Please enter a character:')

#Conditional expressions
if character.lower() in vowels:
    print("The character '", character, "' is a vowel.")
elif character in digits:
    print("The character '", character, "' is a digit.")
elif character in punctuation:
    print("The character '", character, "' is punctuation.")
else:
    print("The character '", character, "' is a consonant.")


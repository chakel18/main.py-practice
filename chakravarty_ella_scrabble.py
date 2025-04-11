"""
Scrabble
Ella Chakravarty

Program calcualtes the scrabble point value of a word from user input.
"""
#create a dictionary to link characters to point values
character_values = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

#dictionary for stop words
stop_words = {'quit', 'q'}

#function to calculate the score of the word
def calculate_score(word):
    return sum(character_values.get(letter.upper(), 0) for letter in word)

#prompts user for input, terminates if stop word, formats the output
def scrabble():
    while True:
        word = input(':>').strip() 
        if word in stop_words:
            break
        print(f'{word} is worth {calculate_score(word)} points.')

#calls the function to start the game
scrabble()
"""
Word Frequency
Ella Chakravarty

Program returns how frequently specific words are used from a string in user input. 

"""

#Creates frequency dictionary from a list of words
def build_dictionary(word_list):
    freq_dict = {} #initialize with empty dictionary
    for word in word_list:
        word = word.lower() #ensures case insentivity
        freq_dict[word] = freq_dict.get(word, 0) + 1 #counts each word
    return freq_dict

#reads input, builds dictionary, prints frequencies
def word_frequency():
    text = input(':>') #Prompts user for statement
    words = text.split() #splits text into words
    freq_dict = build_dictionary(words) #builds frequency dictionary
    print("Word List: ")
    print(words)
    print('Bag of Words:')
    for words in sorted(freq_dict.keys()): #iterate through sorted words
        print(f'{words} - {freq_dict[words]}')

#call function to start
word_frequency()

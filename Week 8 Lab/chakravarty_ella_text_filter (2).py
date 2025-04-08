"""
Text Filter
Ella Chakravarty

Program moderates content in message and filters banned words. 
"""

#define text_filter function
def text_filter(message):
    banned_words = {"Turkey", "Dog", "Fox", "Cat", "Chicken"}
    words = message.split()
    filtered_words = []

#in membership operation to filter words from list
    for word in words:
        if word not in banned_words:
            filtered_words.append(word)

    return " ".join(filtered_words)

#Format input and output messages
message = input(">: ")
print("Input message: ", message)
filtered_message = text_filter(message)
print("Output message: ", filtered_message)

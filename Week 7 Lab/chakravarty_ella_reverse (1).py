"""
Reverse
Ella Chakravarty

Program reverses line of text from input.
"""

#Use range to reverse statement, define new string
def reverse_string(text):
    reverse_string = ''
    for i in range(len(text) -1, -1, -1):
        reverse_string += text[i]
    return reverse_string

#Prompt user for input
string = input('Please Enter Your String:')

#Program terminates under condition
while string not in ['Quit','quit', 'q']:
    print('Reversed:', reverse_string(string))
    string = input('Please Enter Your String:')

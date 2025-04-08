"""
Password
Ella Chakravarty

Program strengthens simple user passwords by replacing specific characters.

"""
#Prompt user for password and assign variable
password = input('Please Enter Your Password:')

#new password assignment
new_password = ''

#creating loop variable before loop
i = 1

#Replace specific characters and add '!' to end
for pass_char in password:
    if pass_char == 'o':
        new_password += '0'
    elif pass_char == 'i':
        new_password += '1'
    elif pass_char == 'a':
        new_password += '@'
    elif pass_char == 'e':
        new_password += '3'
    elif pass_char == 'A':
        new_password += '4'
    elif pass_char == 'B':
        new_password += '8'
    elif pass_char == 's':
        new_password += '$'
    else:
        new_password += pass_char

#Increment loop variable
i = i + 1

#append input string
new_password += '!'

#Formatting the output
print('Your new strong password is:', new_password)
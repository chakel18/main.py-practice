"""
Phone
Ella Chakravarty

Formats a 10-digit phone number with the area code, prefix, and line number using the format (800) 555-1212. 

"""

#Formatting the input
phone_number = int(input('Please enter your phone number:'))

#Ordering expressions
line_number = phone_number % 10000
phone_number //= 10000
prefix = phone_number % 1000
phone_number //= 1000
area_code = phone_number

#Formatting the output
print(f'({area_code}){prefix}-{line_number}')

''' 
    WAP to check a password is secure or not.
    - 1. password must contains minimim 14 char.
    - 2. both upper and lower case, upper min 3, lower min 5.
    - 3. must contains 3 number and 3 special char.
'''

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
password = input("Enter your password :: ")

def validate(values):
    for letter in password:
        if letter in values:
            return True
    return False  # optional

if len(password) >= 8:
    if validate(ascii_lowercase):
        if validate(ascii_uppercase):
            if validate(digits):
                if validate(punctuation):
                    print("Password VALID !!!! :) ")
                else:
                    print("minimim one special char required")
            else:
                print("Minimum 1 digits required !")
        else:
            print("Minimum 1 upperCase letter required")
    else:
        print("Minimum 1 lowerCase letter required !")
else:
	print("Password must contains minimim 8 char.")

'''
# Simple method
if len(password) >= 8 and validate(ascii_lowercase) and validate(ascii_uppercase) and validate(digits) and validate(punctuation):
    print("Valid password !")
else:
    print("Password must contains - min 8 char, one lowercase, one uppercase, one digit and one special char")
'''

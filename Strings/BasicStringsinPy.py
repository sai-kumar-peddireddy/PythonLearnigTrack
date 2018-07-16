"""
Sun Jul 15 04:54:24 IST 2018

This program will ilastruate about the basics of string

Srings are immutable so we can't change the value of string

source :- https://www.geeksforgeeks.org/interesting-facts-about-strings-in-python-set-1/

"""

string1 = "this is a string1"

print(string1)

# string1[5] = '2'   this gives an error strings are immutable

string1 = string1 + " concatenation"

""" here the value of string is changed that is we concatinated the string and reassigned to the same string varable
    but once string is assignd we can't change it's value. in this case a new string is created and asigned to string1 
    variable
"""

print(string1)

print("-----------------------------------")

# different types of creating a string

string2 = 'single quoted string'

string3 = "double quoted string"

string4 = '''Triple quoted string
             so we can write in
             multiple lines'''
print(string2, '\n', string3, '\n', string4)



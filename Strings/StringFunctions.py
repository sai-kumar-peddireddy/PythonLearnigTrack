"""
Sun Jul 15 14:47:37 IST 2018
source:-
https://www.geeksforgeeks.org/python-string-methods-set-1-find-rfind-startwith-endwith-islower-isupper-lower-upper-swapcase-title/
https://www.geeksforgeeks.org/python-string-methods-set-2-len-count-center-ljust-rjust-isalpha-isalnum-isspace-join/
https://www.geeksforgeeks.org/python-string-methods-set-3-strip-lstrip-rstrip-min-max-maketrans-translate-relplace/

"""

"""
find returns the position of a substring in first occurrence  within a string if it founds.
it takes 3 argument's substring ,start position and end position.
start position and end position are operational  parameters start position = 0 and end position = length of string  
"""

name = "sai kumar peddireddy"

print(name.find("kumar"))

print(name.find("abc"))

print(name.find("dd", 11, 16))

"""
rfind() returns the position of last occurrence
"""
print(name.find("dd"))
print(name.rfind("dd"))

if name.startswith("sai"):
    print(name, "starts with sai")
else:
    print(name, "not starts with sai")

if name.endswith("peddireddy"):
    print(name, "ends with peddireddy")
else:
    print(name, "not ends with peddireddy")

if name.islower():
    print(name, "contains all lower case letters")
else:
    print(name, "does't contain all lower case letters")
if name.isupper():
    print(name, "contains all lower case letters")
else:
    print(name, "does't contain all upper case letters")

print("name.lower()", name.lower())

print("name.upper()", name.upper())

uppercase_str = "UPPERCASE letters"

lowercase_str = "lower case letters"
# swapcase() converts the lowercase letters to upper and upper case letters to lower

print("uppercase_str.swapcase():", uppercase_str.swapcase())

print("lowercase_str.swapcase()", lowercase_str.swapcase())
#  title() converts first letter of every word of string is upper cased and else all are lower cased.

print(name.title())

#  len prints the length of string
print("len(name)", len(name))

"""
count() will take 3 arguments substring, start position and end position
returns number of occurrences of substring in main string   
"""

print("in", name, "dd found in ", name.count("dd"), "places")

"""
center() function ued to enclose the string with given character by keeping the string center to the length of string 
by default it takes space as a character    
"""

print(name.center(30, '_'))

"""
ljust()
This function returns the original string shifted to left that has a character at its right. It left adjusts the string.
By default the character is space. It also takes two arguments, length of string and the character
rjust()
This function returns the original string shifted to right that has a character at its left. It right adjusts the 
string.By default the character is space. It also takes two arguments, length of string and the character.
"""
print(name.ljust(25, '_'))

print(name.rjust(25, '_'))

"""
 isalpha() :- This function returns true when all the characters in the string are alphabets else returns false.
            if it contains other  than alphabets returns false ex:- space , special characters  
 isalnum() :- This function returns true when all the characters in the string are combination of numbers and/or
 alphabets else returns false.

 isspace() :- This function returns true when all the characters in the string are spaces else returns false.
 
 join() :- This function is used to join a sequence of strings mentioned in its arguments with the string.

"""
string = "77"
print(string, "isalnum()", string.isalnum())

print(string, "isalpha()", string.isalpha())

print(name, "isalpha()", name.isalpha())
spaces = "                 "

print("spaces.isspace()", spaces.isspace())

"""
join() :- This function is used to join a sequence of strings mentioned in its arguments with the string.
"""
s1 = "_"

s2 = ("sai", "kumar", "peddireddy")
print(s1.join(s2))


# Mon Jul 16 04:59:13 IST 2018
"""
strip() :- This method is used to delete all the leading and trailing characters mentioned in its argument
"""
s3 = "!!!String!!!!"

print(s3.strip('!'))

print(s3.lstrip('!'))

print(s3.rstrip('!'))

"""
min(“string”) :- This function returns the minimum value alphabet from string.
max(“string”) :- This function returns the maximum value alphabet from string.
"""
s4 = "abcdef"
print(min(s4))

print(max(s4))
"""
maketrans() :- It is used to map the contents of string 1 with string 2 with respective indices to be translated later
 using translate().

translate() :- This is used to swap the string elements mapped with the help of maketrans().
"""

source = "this is a string"

def1 = "thsarng"

def2 = "1234567"

rule = str.maketrans(def1, def2)

print(source.translate(rule))

"""
replace() :- This function is used to replace the substring with a new substring in the string. This function has 3 
arguments. The string to replace, new string which would replace and max value denoting the limit to replace action 
( by default unlimited ).
"""
str1 = "cat dog elephant zoo monkey cat dog dog"
print("beforereplace:", str1)
s2 = "dog"
s3 = "cat"

print("after replace:", str1.replace(s2, s3, 2))  # 3rd we will howmany times we can replace
print("after replace:", str1.replace(s2, s3))   # if not specifiy 3 argumnet means replace all

"""
expandtabs() :- It is used to replace all tab characters(“\t”) with whitespace or simply spaces using the given
tab size, which is optional to supply.
"""
s1 = "cat\tdog\telephant\tzoo\tmonkey\tcat\tdog\tdog"

print(s1.expandtabs())

print(s1.expandtabs(2))  # expanding tab with 2 spaces

print(s1.expandtabs(3))  # expanding tab with 3 spaces

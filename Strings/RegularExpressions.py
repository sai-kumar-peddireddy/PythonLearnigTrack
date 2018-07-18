"""
Wed Jul 18 06:51:30 IST 2018
source :-https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
Regular Expressions are used to detect a pattern in a string and do some operations on it
Function compile()
Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for
pattern matches or performing string substitutions.
"""
import re

pattrenObj = re.compile('[a-e]')  # comple returns a pattren object which have different methods

print(pattrenObj.findall('Hi Mr.Sai kumar peddireddy, how is your python learning expreaince '))
print("---------------------------")
# find all function will find based on regular expression in given string
# this fill print all a,b,c,d,e occurrence in given string

pattrenObj = re.compile('\d')  # \d finds all the digits

print("\d: ", pattrenObj.findall("Hi your Account Bal is 4445334 for end of the day 18/07/2018"))
print("---------------------------")

pattrenObj = re.compile('\d+')  # \d+ finds all the group digits one or more

print("\d+: ", pattrenObj.findall("Hi your Account Bal is 4445334 for end of the day 18/07/2018"))
print("---------------------------")


pattrenObj = re.compile('\w')  # \w finds all the all the alphanumerics a-z, 0-9, A-Z

print("\w: ", pattrenObj.findall("Hi your Account Bal is 4445334 for end of the day 18/07/2018"))
print("---------------------------")

pattrenObj = re.compile('\w+')  # \w finds all the all the group of alphanumerics a-z, 0-9, A-Z one or more

print("\w+: ", pattrenObj.findall("Hi your Account Bal is 4445334 for end of the day 18/07/2018"))
print("---------------------------")

pattrenObj = re.compile('\W')  # \W finds all the all the non alphanumerics

print("\W: ", pattrenObj.findall("Hi your Account Bal is 4445334 for end of the day 18/07/2018"))
print("---------------------------")

pattrenObj = re.compile('\W+')  # \W finds all the group of non alphanumerics one or more

print("\W+: ", pattrenObj.findall("Hi your Account Bal is 4445334 for end of the day 18/07/2018 **"))
print("---------------------------")

pattrenObj = re.compile('ap*')
"""
Our RE is ap*, which ‘a’ accompanied by any no. of ‘b’s, starting from 0.
ou put is ['app', 'a', 'app']
app -> a with 2 p's
a   -> a with 0 p's
app -> a with 2 p's
"""

print("ap*: ", pattrenObj.findall("apple came from apple tree"))
print("---------------------------")

"""
split()
Split string by the occurrences of a character or a pattern, upon finding that pattern,
the remaining characters from the string are returned as part of the resulting list.
syntax :- re.split(pattern, string, maxsplit=0, flags=0)
"""

print(re.split("\W", "hey What's up dude!!!"))  # this will print splited string which is based on all non alphanumeric

print(re.split("\W+", "hey What's up dude!!!"))  # this will print splited string which is based on all non alphanumeric


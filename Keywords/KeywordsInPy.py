"""
Sat Jul 14 06:13:15 IST 2018
source: https://www.geeksforgeeks.org/keywords-python-set-1/

This program will talk about what are the different keywords in Python language
keyword module has mainly to functions
1.kwlist :-kwlist will return the list of keywords in Python.
2.iskeyword:-iskeyword will tell given string is keyword or not by returning bool value.

"""

import keyword

print("these are the different keywors in python")

print(keyword.kwlist)

print("is 'if' is a keyword:",keyword.iskeyword("if"))

print("is 'hi' is a keyword:",keyword.iskeyword("hi"))

print("is 'fi' is a keyword:",keyword.iskeyword("fi"))

print("is 'True' is a keyword:",keyword.iskeyword("True"))

print("is 'False' is a keyword:",keyword.iskeyword("False"))

print("is 'true' is a keyword:",keyword.iskeyword("true"))
# here 'true' is not keyword because keyword is this 'True' same with below satement

print("is 'false' is a keyword:",keyword.iskeyword("false"))
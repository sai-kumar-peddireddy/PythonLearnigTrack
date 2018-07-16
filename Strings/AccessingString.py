"""
Sun Jul 15 05:21:28 IST 2018

this program will tell about how to access the string
string index will start from 0 which denotes starting of the index
-ve index -1 will start from the end of the string
it will check out of range
-> Slicing
    string_name[beginning: end : step]

source:- https://www.geeksforgeeks.org/interesting-facts-about-strings-in-python-set-2/
"""
name = "sai kumar peddireddy"

print(name[0], '\t', name[-1])  # starting and ending of a string

print(name[4], '\t', name[-5])

# print(name[20]) IndexError: string index out of range

print("------------------------------")

# Slicing
print("Slicing")

print(name[1:5])

print(name[-7:-3])

print(name[-10:-3])

print(name[2:10:2])

print(name[1:len(name):2])  # printing the odd positions in string

print(name[0:len(name):2])  # printing the evevn positions in string

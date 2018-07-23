"""
Mon Jul 23 04:35:02 IST 2018
source :- https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/
ListComprehension:-
    We can create lists just like mathematical statements and in one line only.
Syntax
    A list comprehension generally consist of these parts :
   Output expression,
   input sequence,
   a variable representing member of input sequence and
   an optional predicate part.
"""
l1 = [i for i in range(10)]  # a list with 9 numbers
print("numbers:", l1)

l1 = [i for i in range(10) if i % 2 == 0]  # a list with even numbers
print("even numbers", l1)

l1 = [i ** 2 for i in range(10)]  # a list with squares
print("squares", l1)

s1 = "sai kumar 243"

l1 = [i for i in s1 if i.isdigit()]  # a list with numbers from string
print("digits from string", l1)

l1 = [i for i in s1 if i.isalpha()]
print("alphabets from string to list", l1)

l1 = [i.upper() for i in s1]
print("list with capital letters of each character in string", l1)

a = 7
l1 = [[a, b, a*b] for b in range(1, 11)]  # multiplication table
i = 0

while i < len(l1):
    print(l1[i])
    i += 1

"""
Fri Jul 27 05:34:34 IST 2018
source : https://www.geeksforgeeks.org/partial-functions-python/

"""
from functools import partial


def func(a, b, c):
    print(a, b, c)
    return a + (b*2) + (c*3)


f = partial(func, 1, 2)   # created f with 2 arguments

print(f(10))
print("--------------------")


g = partial(func, c=10, b=20)  # as per the variable names values got assigned not based on the order of argumnets

print(g(30))
print("--------------------")

# global variables
b = 25
c = 15

h = partial(func, c, b)  # here variables are assigned based on order not by name because we declared local variables
print(h(10))
print("--------------------")

i = partial(func, c=5)

print(i(b, 4))   # here argumnet is passed on position  here b is assigned to a in func argumnets


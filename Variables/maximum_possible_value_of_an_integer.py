"""
Fri Jul 27 03:47:26 IST 2018
source : https://www.geeksforgeeks.org/what-is-maximum-possible-value-of-an-integer-in-python/

In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available
memory

Thus we never need any special arrangement for storing large numbers (Imagine doing above arithmetic in C/C++).

in Python 3, there is only one type “int” for all type of integers how big number maybe

In Python 2.7. there are two separate types “int” (which is 32 bit) and “long int” that is same as “int” of Python 3.x,
i.e., can store arbitrarily large numbers.
"""
import sys


a = 10
print("a =", a, "type(a)", type(a))

b = 19991762877764778

print("b =", b, "type(b)", type(b))

c = 100**100

print("c =", c, "type(c)", type(c))

d = 555555544115.985776

print("d =", d, "type(d)", type(d))

print("maximum value of a float", sys.float_info.max)


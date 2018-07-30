"""
Mon Jul 30 21:10:41 IST 2018
source https://www.geeksforgeeks.org/inplace-vs-standard-operators-python/

Inplace operators behave similar to normal operators except that they act in a different manner in case of
mutable and Immutable targets.

_iadd_ method also takes two arguments, but it makes in-place change in 1st argument passed by storing the sum in it.
As object mutation is needed in this process, immutable targets such as numbers, strings and tuples, shouldn’t have
 _iadd_ method.
"""

import operator

a = 10
b = 15

# inplace in immutable
x = operator.add(a, b)  # normal addition which is similar to x = a+b

print("a =", a, "b =", b, "\noperator.add(a, b)=", x)
print("a =", a, "b =", b)
print("--------------------")
operator.iadd(a, b)  # inplace operator iadd which is similar to a = a+b or a+= b but this does't work on immutable

print("a =", a, "b =", b)
print("--------------------")
# inplace operator  in mutable objects

li = [12, 15, 25, 85, 98]

print("operator.add", operator.add(li, [5, 4, 3]))  # here the original ist is not changed

print("li", li)

# inplace operator which is similar to li = li + [1, 2, 3, 4]

print("operator.iadd()", operator.iadd(li, [1, 2, 3, 4]))


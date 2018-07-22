"""
Sun Jul 22 15:13:47 IST 2018
source :- https://www.geeksforgeeks.org/python-docstrings/
It’s specified in source code that is used, like a comment, to document a specific segment of code.
Unlike conventional source code comments, the docstring should describe what the function does, not how.
"""


def additionfun(parm1, parm2):
    """
    This is a Doc string here we can say how to use this function.
    this function returns sum of 2 numbers
    :param parm1: pass any number
    :param parm2: pass any number
    :return:sum of 2 numbers
    """
    return parm1 + parm2


print("usage of doc String  __doc__")

print(additionfun.__doc__)
print("----------------------------")
print("by help():")

help(additionfun)

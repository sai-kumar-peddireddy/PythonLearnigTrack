"""
Fri Jul 27 06:49:42 IST 2018
source: https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
We use two operators * (for tuples) and ** (for dictionaries).

Consider a situation where we have a function that receives four arguments.
We want to make call to this function and we have a list of size 4 with us that has all arguments for the function.
If we simply pass list to the function, the call doesn’t work.
We can use * to unpack the list so that all elements of it can be passed as different parameters.
When we don’t know how many arguments need to be passed to a python function, we can use Packing to pack all arguments
in a tuple.

"""


def funtoprint(a, b, c):
    print(a, b, c)


lst = [5, 10, 30]

funtoprint(*lst)  # unpacking from list

for i in range(*lst[0:2]):    # passing range argumnets from list using unpacking
    print(i)


def funonpacking(*args):
    print(args)
    s = 0
    for i in args:
        s = i + s
    print("sum ", s)


funonpacking(6, 7, 8, 9, 10)


def funondct(name, age, uid):
    print(name, age, uid)


# d = {'p': 1, 's': 2, 'I': 25}  this gives you error because variable names and keys must match

d = {'name': "Sai kumar", 'age': 23, 'uid': 10}

funondct(**d)  # packing


def fundectmultiplrargs(**args):
    print(type(args))
    print(args)
    for k, v in args.items():
        print("values", args[k])


fundectmultiplrargs(apple=5, orange=10, comments="i think everthing is fine")  # key = value


"""
Sun Jul 29 04:56:17 IST 2018
source : https://www.geeksforgeeks.org/type-conversion-python/
         help('int')

"""

val = "1010"  # binary number in string
"""
class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4

"""
intval = int(val, 2)

print("string", val, "binary value", intval)

# float() converts any number or string to float
print("int val", intval, "->", float(intval), "strng val", val, "->", float(val))

c = '7'

# ord() Return the Unicode code point for a one-character string
print(c, "->", ord(c))

# hex() Return the hexadecimal representation of an integer
print(intval, "->", hex(intval))

# oct() Return the octal representation of an integer
print(intval, "->", oct(intval))

name = "sai kumar"

# tuple() converts into tuple
print("string", "-> tule", tuple(name))

# list() converts into list
print("string", "-> list", list(name))

# set() converts into tuple
print("string", "-> set", set(name))

"""
dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
"""

tupval = (('a', 5), ('b', 6), ('d', 7), ('e', 8))

print("\n", tupval, "\ntupval to dict\n", dict(tupval))

"""
complex(real[, imag]) -> complex number
 |  
 |  Create a complex number from a real part and an optional imaginary part.
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.

"""

print("complex(10,5)", complex(10, 5))

"""
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
"""

print("string(\"15\")", str("15"))


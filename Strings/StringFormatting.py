"""
Mon Jul 16 06:46:26 IST 2018
source:- https://www.geeksforgeeks.org/string-formatting-in-python-using/
http://www.bogotobogo.com/python/python_string_formatting.php
"""
floatval = 10.56
print(floatval)
string = "float variable in string as float %f,right justified:%8f, right justified starting with 0:%08.2f \
right justified with '+'sign :%+08.2f," % (floatval, floatval, floatval, floatval)

print(string)

intval = 65
print("intval:", intval)
# '-' denotes left justification and '0' denotes 0 fills
string = "intval variable in string as int %d ,left justified 6 :%-6d,zero fills %06d" % (intval, intval, intval)

print(string)


string = "intval variable in string as char %c" % intval  # it will print 'A' ASCII value (65)

print(string)

string = "intval variable in string as octal %o" % intval

print(string)

string = "intval variable in string as hexa %x" % intval

print(string)

string = "intval variable in string as hexa %X" % intval

print(string)

string = "intval variable in string as Exponent %e" % intval

print(string)

string = "intval variable in string as Exponent %E" % intval

print(string)


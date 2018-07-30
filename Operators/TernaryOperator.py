"""
Sun Jul 29 06:30:26 IST 2018
ternary operator
source : https://www.journaldev.com/17225/python-ternary-operator
         https://www.geeksforgeeks.org/ternary-operator-in-python/
syntax:
    [when_true] if [condition] else [when_false]
    for tiple
        (when_false, when_true)[condition]

"""

text = str()

# ternary operator
text = "true block" if True else "else block"

print(text)

a = 5
b = 25
minval = a if a < b else b
print(minval)

maxval = a if a > b else b
print(maxval)

# (when_false, when_true)[condition] tupple

t = ('false block', 'true block')[True]

print(t)

t = ('falseblock', 'true block')[False]

print(t)

"""
Sat Jul 14 15:28:37 IST 2018
This program will show basic syntax of differnt loops
source :- https://www.geeksforgeeks.org/loops-and-loop-control-statements-continue-break-and-pass-in-python/
          https://docs.python.org/3/tutorial/controlflow.html

basically for is used for iterate through string list tuple or other iterable objects
"""

# while loop
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("else part is executed when ever expression fails in loop ")
    print("in else block value of i is:", i)

print("------------------------------------------")
# for loop

for i in range(10):
    print(i)
else:
    print("else part is executed when ever expression fails in loop ")
    print("in else block value of i is:", i)

print("------------------------------------------")
# iterate through the string
name = "sai kumar "

for i in name:
    print(i)

print("------------------------------------------")
# break statement
for i in name:
    if i == 'a':
        break
    print(i)
else:
    print("this is else for break this not going to appear")
print("------------------------------------------")
# continue statement
for i in name:
    if i == ' ':
        continue
    print(i)
else:
    print("this is else for continue this  going to appear")

print("------------------------------------------")

for i in range(5):
    print(i)
    i = 10  # this line will not be effected because i value is overwritten with index range
    print(i)




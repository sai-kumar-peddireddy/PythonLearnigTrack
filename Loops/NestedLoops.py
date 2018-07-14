"""
Sat Jul 14 18:12:47 IST 2018
this program will show the behaviour of nested loop
here i am trying to print the following pattern
1
2 2
3 3 3
4 4 4 4
"""

val = int(input("please enter the value:"))

for i in range(val):
    for j in range(i):
        print(i, end=' ')
    print("")


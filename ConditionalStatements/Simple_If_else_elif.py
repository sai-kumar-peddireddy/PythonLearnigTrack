'''
Sat Jul 14 08:18:37 IST 2018

this progrm will tells you useage of if,elif,else in python

Here i am finding the smallest of 3 nubers
'''

a = 15
b = 12
c = 11

if ( a < b):
    if( a < c ):
        print(a,"is smaller than ",b,c)
elif( b < c):
    print(b,"is smaller than the",a,c)
else:
    print(c,"is smaller than the ",a,b)

#09/07/2018
'''
Math related functions in python
'''
import math

print('addition')
print('2+3 = ',2+3)

print('subtraction')
print('2-3 = ',2-3)

print('multiplication')
print('2*3 = ',2*3)

print('division')
print('2/3 = ',2/3)

print('modulus')
print('2%3 = ',2%3)

'''
ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
'''
print(math.ceil(10.1)) #11

print(math.ceil(-10.1)) #-10

'''
 copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
        it simply copies sign of the another number and returns float value
'''

print(math.copysign(10.5,1))

'''
exp(x, /)
        Return e raised to the power of x.
        value of exponent is e = 2.718
'''

print(math.exp(5)) #E^5


#Tue Jul 10 06:09:44 IST 2018

print(math.fabs(-10.2))

print(math.factorial(4))
'''
floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.


'''
print(math.floor(10.2))#10
print(math.floor(10.9))#10
print(math.floor(-10.2))#11
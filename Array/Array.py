"""
Wed Jul 25 04:46:38 IST 2018
source : https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
Array
    we can declare a array of specific data type in python to manupulate a single datatype eleents of in array
    to work on array we need to imort Array module
    refer https://docs.python.org/3/library/array.html
"""

import array  # importing array module

arr = array.array('i')  # array of integers  without initialization

# arr = array('i', [1, 2, 3])   array of integers  with initialization

for i in range(10, 100, 10):
    arr.append(i)   # used insert elemnet at the last
print(arr)

arr.insert(0, 11)  # insert element at given position
print(arr)

# printing an Array based on index
print("Array:")
i = 0
while i < len(arr):
    print(arr[i], "\t", end='')
    i += 1
print()

arr.pop()  # pops element at given position or deletes last element in array

arr.pop(3)  # 30 poped

arr.remove(50)  # removes first occurrence of given element 50 removed

print(arr)  # 90 poped

print(arr.index(20))  # gives the index of first occurrence of give element

arr.reverse()  # reverse array

print(arr)

print("arr.typecode", arr.typecode)   # gives array data type

print("arr.itemsize", arr.itemsize)  # gives size of each element

print("arr.buffer_info()", arr.buffer_info())   # gives a tuple contains addres and number of elements in it

print("arr.count(11)", arr.count(11))   # number of occurrences of given element in array

arr2 = array.array('i', [22, 35, 66])

"""
appends a whole array mentioned in its arguments to the specified array.
it extend calling array with given array or it appends an array which is specified in argumnet
"""
arr2.extend(arr)

print(arr2)

l1 = [65, 76, 89, 39]

arr.fromlist(l1)  # it appends list at end of the array
print(arr)

l1 = arr.tolist()  # it returns array elemnets in list format

print("List from array:", l1)

#  slicing
print("arr[0]", arr[0])
print("arr[0:-2]", arr[0:-2])



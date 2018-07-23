"""
Mon Jul 23 06:00:09 IST 2018
source
    https://www.geeksforgeeks.org/list-methods-in-python-set-1-in-not-in-len-min-max/
    https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/

"""

l1 = [1, 5, 7, 9, 6, 4, 3]

if 5 in l1:  # in operator finds given element is in list or not. if present return true or false
    print("5 is present in list")
else:
    print("5 is not present in list")

# not in operator finds given element is not in list or not. if element not present return true or false
if 10 not in l1:
    print("10 is not in list")
else:
    print("10 is present in list")

# len gives the length of the list
print("length:", len(l1))

print("min:", min(l1), "max:", max(l1))  # min max of list

l2 = [5, 48, 75, 26]

l3 = l1 + l2   # + operator concatenate two lists
print(l3)

l3 = l1 * 2  # * operator multiplies the list and gives a single list
print(l3)

"""
index(element, begin, end)
it returns the first occurence index of a given elemnet in the list of after begin and before end  
if element is not present returns value error
"""
print(l3.index(5))
print(l3.index(5, 7))
print(l3.index(5, 7, 10))
# print(l3.index(22)) ValueError: 22 is not in list

"""
count(element)
    count will return number of occurences of a elemnet in list
"""
print("count(5):", l3.count(5))
"""
del list[start:end]
del delets the list based on given positions  includeing start and end positions in list 
"""
print("before del", l3)
del l3[6:]
print("after del", l3)

"""
pop(position)
    it deletes the element of a given postion and returns the element   
"""
print("pop:", l3.pop(2))
print(l3)
print(l3.pop())  # if not specify any element it removes last element in list

"""
insert(position, element)
    it inserts fiven element at given position
"""
l3.insert(4, 22)
print(l3)

l3.remove(22)  # it removes the first occurence ofgiven element
print(l3)

l3.sort()  # sorts the list in assending order
print(l3)

l3.sort(key=None, reverse=True)  # sorts list in descending order
print(l3)

l3.reverse()  # reverse the list
print(l3)
"""
extend(list) 
    it extends list with of list mentioned in parameter 
"""
print(l3)
l3.extend(l2)
print(l3)

"""
append(element)
    appends the given elemnet at end of list 
"""
l3.append(12)
print(l3)

print("sum of l3 list:", sum(l3))  # it returns sum
print("min of l3", min(l3), "\tmax of l3", max(l3))  # min max of lists

"""
clear 
    removes all the elements in list
"""
l1.clear()
l2.clear()
l3.clear()
print(l1, l2, l3)


"""
Tue Jul 24 06:09:45 IST 2018
source: https://www.geeksforgeeks.org/sets-in-python/
Sets
    A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
    The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking
    whether a specific element is contained in the set.
    This is based on a data structure known as a hash table.
    represented in {}
Frozen Sets
     Frozen sets are immutable objects that only support methods and operators that produce a result without
     effecting the frozen set or sets to which they are applied
"""

s = {"sai", "kumar", "peddireddy"}  # normal set
s.add("Male")  # adding an elemnt
print(s)

frozen_set = frozenset(["name", "age", "sex"])
print(frozen_set)
print("--------------------")
"""
frozen_set.add("place") we can't add element to frozenset.
error AttributeError: 'frozenset' object has no attribute 'add'
"""
# methods on sets

citys = {"Hyderabad", "Amaravathi", "Bangalore"}

citys.add("kochi")  # adds an elemnt to set
print(citys)
print("--------------------")

places = {"visakhapatnam", "kakinada", "Hyderabad"}

all_places = citys.union(places)  # gives the union of two sets set1.union(set2)
print("union of \n", citys, "\n", places, "\nis", all_places)
print("--------------------")
all_places = {}

# or operator gives the union
all_places = citys | places
print("union of \n", citys, "\n", places, "\nis", all_places)
print("--------------------")

intersect = all_places.intersection(citys)
print("intersection of \n", all_places, "\n", citys, "\nis", intersect)
print("--------------------")
intersect = {}

# and operator gives the intersection
intersect = all_places & citys
print("intersection of \n", all_places, "\n", citys, "\nis", intersect)
print("--------------------")

"""
difference(s) Method: Returns a set containing all the elements of invoking set but not of the second set.
 We can use ‘-‘ operator here
"""
diff = all_places.difference(citys)
print("difference of \n", all_places, "\n", citys, "\nis", diff)
print("--------------------")
diff = {}

diff = all_places - citys  # operator '-' for diff
print("difference of \n", all_places, "\n", citys, "\nis", diff)
print("--------------------")

# clear method clears all the elemnts in set

diff.clear()
intersect.clear()
all_places.clear()
citys.clear()
s.clear()

set1 = set()
set2 = set()

for i in range(1, 6):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

print("set1", set1, "\nset2", set2)

set3 = set1 & set2  # intersection
print("set3", set3)

if set1 > set2:
    print("set1 is super set of set2")
elif set2 < set1:
    print("set2 is subset of set1")
else:
    print("no relation between them")


if set2 > set3:
    print("set2 is super set of set3")

if set3 < set2:
    print("s3 is subset of set2")

print("difference between set2 and set1 is ", set2 - set1)

set4 = {55, 65}
if set4.isdisjoint(set3):
    print("set4 and set3 has nothing common elemnets")

if set2.isdisjoint(set3):
    print("set2 and set3 has nothing common elemnets")

set3.clear()
set2.clear()
set1.clear()


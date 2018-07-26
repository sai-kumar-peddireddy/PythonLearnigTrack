"""
Thu Jul 26 07:11:59 IST 2018
source: https://www.geeksforgeeks.org/ordereddict-in-python/
OrderedDict
    An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.
    The only difference between dict() and OrderedDict() is that:
"""
from collections import OrderedDict

dc = {}

dc['sai'] = 1
dc['nagesh'] = 2
dc['durga'] = 3

for k, v in dc.items():
    print(k, v)

print("---------------")

odc = OrderedDict()

odc['lalitha'] = 1
odc['anusha'] = 2
odc['sai'] = 3
odc['sai2'] = 4

for k, v in odc.items():
    print(k, v)
print("---------------")
# If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.

odc['sai'] = 5

for k, v in odc.items():
    print(k, v)
print("---------------")

# Deleting and re-inserting the same key will push it to the back as OrderedDict however maintains the order of
# insertion

odc.pop('sai')

for k, v in odc.items():
    print(k, v)
print("---------------")

odc['sai'] = 3

for k, v in odc.items():
    print(k, v)
print("---------------")



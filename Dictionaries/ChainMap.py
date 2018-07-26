"""
Thu Jul 26 06:45:59 IST 2018
source:-https://www.geeksforgeeks.org/chainmap-in-python/
ChainMap
    Python also contains a container called “ChainMap” which encapsulates many dictionaries into one unit.
    ChainMap is member of module “collections“.

"""
import collections
dc1 = {'apple': 50, 'mango': 25}
dc2 = {'orange': 15, 'guva': 5, 'apple': 45}

print(dc1, dc2)

cmap = collections.ChainMap(dc1, dc2)
# when we formed a chain map with 2 dc1,dc2 both has apple as a key it will take  key from 1st argument

print("formed chain map is:", cmap)

print("cmap.keys():", list(cmap.keys()))
print("cmap.values():", list(cmap.values()))

print("value of apple before reverse:", cmap['apple'])

# This function reverses the relative ordering of dictionaries in the ChainMap. refer 14line
cmap.maps = reversed(cmap.maps)

print("value of apple after reverse:", cmap['apple'])

dc3 = {'grapes': 25, 'kiwi': 75}

# new_child() :- This function adds a new dictionary in the beginning of the ChainMap returns new chain map
cmap2 = cmap.new_child(dc3)
print(cmap)
print(cmap2)

print("cmap2.keys():", list(cmap2.keys()))
print("cmap2.values():", list(cmap2.values()))

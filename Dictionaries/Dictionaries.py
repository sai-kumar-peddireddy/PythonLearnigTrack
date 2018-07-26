"""
Wed Jul 25 06:22:12 IST 2018
source : https://docs.python.org/3/tutorial/datastructures.html#dictionaries
         help('dict')
Dictionaries
    dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys

    Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
    either directly or indirectly, it cannot be used as a key.

    You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments,
    or methods like append() and extend().
    
"""
# Thu Jul 26 04:48:46 IST 2018


captials = {'Andhra pradesh': 'Amaravati', 'Telangana': 'Hyderabad', 'karnataka': 'Bangalore'}   # dictionary

# accessing

print("captials['Andhra pradesh']", captials['Andhra pradesh'])

# looping

for key, val in captials.items():
    print("key:", key, "value:", val)

print("contents of dictionaries as a string:", str(captials))   # str(capitals) gives dictionary as string

print("contents of dictionaries as a list:", captials.items())   # items() gives dictionary as list

print("len:", len(captials), "type:", type(captials))  # length and type

c1 = {}  # empty dictionary

c1 = captials.copy()  # shallow copy  of  capitals  into c1

print("copied items", c1.items())

dict1 = {'Area': '8525212'}

"""
 update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]

"""
captials.update(dict1)  # update will add all the items of dictionary that passed in argumnet

print("updated capitails:", str(captials))

seq = ('goodweather', 'watersource')  # squance

# fromkeys function Returns a new dict with keys from iterable and values equal to value passed in argumnet
dc1 = {}
dc1 = dc1.fromkeys(seq, 'yes')

print(str(dc1))

print("list of keys", captials.keys())  # keys() return all keys as a list

"""
values(...)
   D.values() -> an object providing a view on D's values
"""
print("list of values", captials.values())  # list of values


# get() will give value of key if it is present if not gives none
print("Andhra pradesh", captials.get('Andhra pradesh'))
print("captials.get('CM')", captials.get('CM'))  # None


"""
setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
  each time a key is absent, a new key is created with the def_value associated to the key passed in arguments.
"""
captials.setdefault('CM', 'CM is not updated')
print("captials.get('CM')", captials.get('CM'))  # gives default value
print("captials.get('CM')", captials.get('PM'))

"""
pop()  remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised
"""
print("captials.pop('karnataka')", captials.pop('karnataka'))

# captials.pop('UP') rises KeyError: 'UP'

"""
popitem(...)
       D.popitem() -> (k, v), remove and return some (key, value) pair as a
       2-tuple; but raise KeyError if D is empty.
       removes last item
"""
print(captials)
print("captials.popitem()", captials.popitem())




c1.clear()  # clearing elements





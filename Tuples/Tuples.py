"""
Tue Jul 24 04:49:08 IST 2018
source : https://www.geeksforgeeks.org/tuples-in-python/
Tuples
    Tuples are similar to lists. repetition, nesting, indexing is similar to list
    Tuples are immutable lists are mutable
    Tuples are represented in ()
"""
t1 = ()  # empty tupple
print(t1, "\tlen(t1)", len(t1))

t = (1, 5, 7, "Sai kumar", "Peddireddy")  # creation of tupple

print("t[0]", t[0])  # accessing tupple
print("t[-1]", t[-1])

#  Slicing tupple
print("t[:-2]", t[:-2])
print("t[::-2]:", t[::-2])
print("t[1:3]", t[1:3])

# printing tupple
for i in t:
    print(i, "\t", end="")

print("\n", t)

# Concatenation of tupples

t2 = ("abc", 2.5, 55, 77)

print("t:", t, "\nt2:", t2, "\nt1+t2:",  t+t2)

# nesting tupples

t3 = (t, t2)

print("t3:", t3)
print("t3[1][0][1:]", t3[1][0][1:])

# repetition

print("t2 * 2 :", t2 * 2)

t4 = t2 * 2
print("t4", t4)

# tuples are immutable when we try to change gives an error

# t4[1] = 2 gives an error

print("len(t3):", len(t3), "\tlen(t3[0])", len(t3[0]))  # finding the length

# conveting list to tupple

li = [1, "!!", 3.33, 1]

t5 = tuple(li)
print("list:", li, "\tlist converted into tupple", t5)

# tuple functions

print("t5.count(1):", t5.count(1))  # counts number of occurrences in tuple

print("t5.index(1):", t5.index(1))  # index of element first  occurrences in tuple

t6 = (1, 5, 9, 0, 89)

print("maximum element max(t6):", max(t6))

print("minimum element min(t6):", min(t6))

t7 = ("abc", "sai", "kumar", "peddireddy")

print("maximum element max(t6):", max(t7))

print("minimum element min(t6):", min(t7))

"""
Sun Jul 29 07:22:54 IST 2018
any(iterable, /)
    Return True if bool(x) is True for any x in the iterable.

    If the iterable is empty, return False.

all(iterable, /)
    Return True if bool(x) is True for all values x in the iterable.

    If the iterable is empty, return True.

"""

mix_list = [True, True, True, True, True, True, True, False, False, False, False]
true_list = [True, True, True, True, True, True]
false_list = [False, False, False, False]

print(any(mix_list))
print("any(true_list)", any(true_list))
print("any(false_list)", any(false_list))
print("any(mix_list[-5:-2])", mix_list[-5:-2], any(mix_list[-5:-2]))



print("all(mix_list)", all(mix_list))
print("all(true_list)", all(true_list))
print("all(false_list)", all(false_list))


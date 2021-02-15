# 40.​ Write a Python program to add an item in a tuple.

tuple1 = (4, 6, 2, 8, 3, 1)
print(tuple1)

tuple1 = tuple1 + (9,)
print(tuple1)

tuple1 = tuple1[:5] + (15, 20, 25) + tuple1[:5]
print(tuple1)

list1 = list(tuple1)

list1.append(30)
tuple1 = tuple(list1)
print(tuple1)

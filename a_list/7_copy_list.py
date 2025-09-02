# 1. Menggunakan .copy()
list1 = [1, 2, 3, 4, 5]
newList1 = list1.copy()
newList1[0] = 0
print(list1)
print(newList1)
print("-" * 30)


# 2. Menggunakan list()
newList2 = list(list1)
newList2[1] = 1
print(list1)
print(newList2)
print("-" * 30)


# 3. Menggunakan Slice Operator
newList3 = list1[:]
newList3[2] = 2
print(list1)
print(newList3)
print("-" * 30)


# 4. Untuk kasus nested list, gunakan deppcopy()
from copy import deepcopy
list2 = [[0, 1], [2, 3], [4, 5], [6, 7]]
newList4 = deepcopy(list2)
newList4[1][0] = 10
print(list2)
print(newList4)
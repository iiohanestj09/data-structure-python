list1 = ["bebek", "ayam", "babi", "kuda", "ayam", "ular", "gajah", "jerapah"]

# A. Menggunakan .remove(item)
list1.remove("bebek")

  # jika terdapat item duplikat yg ingin dihapus, remove akan menghapus item yg lebih awal
list1.remove("ayam")
print(list1)


# B. Menggunakan .pop(index)
list1.pop(3)

  # jika .pop() saja tanpa index, maka pop akan menghapus item terakhir di list
list1.pop()
print(list1)


# C. Menggunakan del list[index]
del list1[1]
print(list1)

  # del juga bisa menghapus seluruh list
del list1
# print(list1)      Error


# D. Menggunakan .clear()  -> membersihkan/mengosongkan isi list
list2 = [1, 2, 3, 4, 5]
print(f"list2: {list2}")

list2.clear()
print(f"list2: {list2}")
# Set -> unordered, unchangeable, unindexed, no duplicate
# walau unchangeable, set bisa remove/pop, add, update dll
# unordered, output dari set tidak beraturan (kadang terurut kadang tidak), karena set bukan urutan inputan dan tidak bisa diandalkan
#! Note: nilai True dan 1 Sama  |  nilai False dan 0 sama di Set, sehingga salah satunya akan disimpan

# Deklarasi Set
set1 = {3, 0, True, False, 2, 1.1, 2.2, 1.1, 3}
print(set1)
print(type(set1))
print(len(set1))

set2 = set(("ayam", "cumi", 2, True, "kambing", "ayam", 2))
print(set2)
print(len(set2))

# akses index  -> karena set dapat berubah-ubah urutannya, maka cukup sulit untuk mengakses item langsung
print(3 not in set1)
print("cumi" in set2)
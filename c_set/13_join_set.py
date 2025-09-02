set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3}
set3 = {"ayam", "babi", "cicak"}
set4 = {4, 5, 6}
#! 1. Union & Update  -> baik Union dan Update sama-sama menghilangkan Duplikat
  # A. .union() : Return new Set & Bisa utk iterable object lainnya
set5 = set1.union(set2)
print(set5)

  # B. | operator : Return new Set & Hanya utk sesama Set
set6 = set1 | set2
print(set6)

set5 = set1.union(set2, set3, set4)     # join multi Set
set6 = set1 | set2 | set3 | set4
print(set5)
print(set6)

  # C. .update() : akan mengubah nilai aslinya.
set1.update(set2)
print(set1)


print("-" * 50)
set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft", "apple"}
#! 2. Intersection  -> Simpan hanya Duplikat
  # A. .intersection() : Return new Set & Bisa utk iterable object lainnya
set7 = set5.intersection(set6)
print(set7)

  # B. & operator : Return new Set & Hanya utk sesama Set
set8 = set5 & set6
print(set8)

set7 = set1.intersection(set5, set6)
set8 = set1 & set5 & set6
print(set7)
print(set8)

  # C. .intersection_update() : akan mengubah nilai aslinya
set1.intersection_update(set5, set6)
print(set1)


print("-" * 50)
#! 3. Difference  -> Simpan item-item dari Set pertama yg tidak dimiliki oleh Set berikutnya
  # A. .difference() : Return new Set & Bisa utk iterable object lainnya
  # B. - operator : Return new Set & Hanya utk sesama set
  # C. .difference_update() : akan mengubah nilai asli Set pertama
set7 = set5.difference(set6)
set8 = set6 - set5
print(set7)
print(set8)


print("-" * 50)
#! 4. Symmetric Difference  -> Simpan item-item yg tidak dimiliki oleh semua Set
  # A. .symmetric_difference() : Return new Set & Bisa utk iterable object lainnya
  # B. ^ operator : Return new Set & Hanya utk sesama set
  # C. .symmetric_difference_update() : akan mengubah nilai asli Set pertama
set7 = set5.symmetric_difference(set6)
set8 = set6 ^ set5
print(set7)
print(set8)
# Tuple -> ordered, unchangeable
# Tuple tidak dapat dimanipulasi isi didalamnya

# Deklarasi Tuple
tuple1 = ("ayam", True, 3, 4.4, "anggur")
tuple2 = tuple(("babi", False, 3.33, 4, "melon"))
print(tuple1)
print(tuple2)
print(type(tuple1))
print(len(tuple1))
# tuple1[2] = 16      Error
# tuple1.append("mangga")   Error

  # Membuat tuple dari 1 elemen
bukanTuple = ("ayam")
iniTuple = ("ayam",)
print(type(bukanTuple))
print(type(iniTuple))


# Bisa akses index walau tidak dapat mengubahnya
print(tuple1[1])
print(tuple1[3])


# Tuple sudah ordered -> Python akan menyimpannya sesuai persis dengan urutannya dibuat, kalau array unordered
list3 = [4, 1, 3, 8, 6, 2]  # 0-4, 1-1, 2-3, 3-8, 4-6, 5-2


# Tuple itu unchangeable, artinya isi di dalamnya tidak daoat diubah-ubah (tambah, hapus, dll). Namun disini letak kerjaanya
  # Kita mengubah tuple -> list, lalu manipulasi di list -> ubah lagi ke tuple
x = (1, 2, 3, 4, 5, 6)
y = list(x)
y.append(7)
y.pop(0)
x = tuple(y)
print(x)
print(y)
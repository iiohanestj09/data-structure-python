dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# 1. Tambah item
  # A. Secara manual
dict1["color"] = "red"

  # B. .update()
dict1.update({"namaPengguna": "Asep"})
print(dict1)
print("-" * 50)


# 2. Hapus item
  # A. .pop(key)
dict1.pop("year")
print(dict1)

  # B. .popitem()  -> menghapus item terakhir
dict1.popitem()
print(dict1)

  # C. .clear()
dict1.clear()
print(dict1)

dict1["coba"] = "hmmm"
  # C. del
del dict1["coba"]
print(dict1)

    # del juga bisa menghapus seluruh dictionary "del dict1"
del dict1
# print(dict1) error
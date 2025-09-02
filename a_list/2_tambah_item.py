# 1. Menggunakan .append()  -> menambah item di akhir
list1 = ["apple", "pinapple", "pen"]
list1.append("watermelon")
list1.append("banana")
print(list1)


# 2. Menggunakan .insert()  -> menambah item sesuai index
list1.insert(0, "grape")
list1.insert(-1, "strawberry")    # hasil akhir indexnya bukan [-1] tapi [-2], karena item asli [-1] bergeser ke kanan 
print(list1)


# 3. Menggunakan .extend()  -> menambah banyak item di akhir
list2 = ["monkey", "elephant", "bird"]
list1.extend(list2)
print(list1)

  # .extend() dapat menambah banyak item selain list, bisa set, tupple, dictionary dll (iterable items)
dict1 = {
    "greet": "haloo",
    "nama": "Putra",
    "tgl": 2
}
list1.extend(dict1)
print(list1)
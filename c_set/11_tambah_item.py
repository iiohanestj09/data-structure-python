# 1. .add()  -> menambah 1 item. Tidak pasti disimpan di urutan mana, karena bawaan set memang unordered
set1 = {3, 0, True, False, 2, 1.1, "ayam", "jangkrik", 3}
set1.add("semangka")
print(set1)


# 2. .update()  -> menambah iterable object (list, tuple, dictonary)
set1.update([9, "kuda", 1.1, "cacing"])     # menambah list
print(set1)

dict1 = {
    "coba": "iya",
    "halo": "hmm"
}

set1.update(dict1)
print(set1)
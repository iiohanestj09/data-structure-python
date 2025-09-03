# Dictionary -> ordered, changeable, not allowed duplicate
# Dictionary menyimpan kumpulan data dengan key: value
# key nya bisa String, Integer, Float, Boolean, Tuple.  List, Set dan Dict tidak bisa
# value nya bisa String, Integer, Float, Boolean, List, Tuple, Set, Dict (nested dict)

# 1. Membuat Dictionary
dict1 = {                                                 # key bisa str, int, float, bool, tuple
    "hewan": "ayam",
    1: 345,
    20.2: (7, 5, 6),
    True: ["a", "p", "a", "i", "y", "a"],
    (3, 4): { 69: "hmm" }
}
dict2 = dict(name= "norway", age= 23, ayam= "hewan")      # key tidak bisa selain string

print(dict1)
print(type(dict1))
print(len(dict1))

print(dict2)
print(type(dict2))
print(len(dict2))
print("-" * 50)


# 2. Akses Item
  # A. Akses literal
print(dict1["hewan"])

  # B. .keys()  -> mengembalikkan semua key di Dict
print(dict1.keys())
print(type(dict1.keys()))

  # C. .values()  -> mengembalikkan semua valuse di Dict
print(dict1.values())
print(type(dict1.values()))

  # D. .items()  -> mengembalikkan semua item yg ada di Dict
print(dict2.items())
print(type(dict2.items))

  # E. Mengecek sebuah key ada
if "name" in dict2:
    print("horeee")
print("-" * 50)


# 3. Mengubah Value
  # A. Secara manual
dict1["hewan"] = "kucheng"
dict1["coba"] = 999             # jika key nya tidak ada, maka akan otomatis ditambahkan dgn valuenya
print(dict1)

  # B. .update()
dict1.update({"hewan": "anjengg"})
dict1.update({"cihuy": 666})    # jika key nya tidak ada, maka akan otomatis ditambahkan dgn valuenya
print(dict1)
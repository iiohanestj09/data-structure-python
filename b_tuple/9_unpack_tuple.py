# Saat kita membuat tuple, biasanya kita memberikan nilai di tuple tersebut. Itu disebut "packing" sebuah tuple
fruits = ("apple", "banana", "orange")    # packing a tuple


# Kita juga bisa "unpacking" sebuah tuple
(red, yellow, orange) = fruits      # harus sama jumlah variabel dan jumlah item di tuple
print(red)
print(yellow)
print(orange)
print("-" * 20)

# Gunakan arterisk  ->  variabel yg menggunakan arterisk akan menjadi list dan mengambil banyak item di tuple
animals = ("monkey", "elephant", "bird", "cow", "cheetah", "lion", "cat", "rat")
(monyet, elephant, *lainnya) = animals
print(monyet)
print(elephant)
print(lainnya)
print("-" * 20)

(*dll, cat, rat) = animals
print(dll)
print(cat)
print(rat)
print("-" * 20)

(monyet2, *etc, rat2) = animals
print(monyet2)
print(etc)
print(rat2)
print("-" * 20)
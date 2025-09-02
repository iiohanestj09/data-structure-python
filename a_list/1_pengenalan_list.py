# 1. Deklarasi List
list1 = ["apple", 2, False, 4.4, "pinapple"]
list2 = list(("grape", 2.2, True, 4, "watermelon"))     # kurung 2 kali (())
print(list1)
print(type(list1))
print(list2)
print(type(list2))
print("-" * 40)

# 2. Akses Item/Elemen
print(f"list1[0]: {list1[0]}")
print(f"list1[-1]: {list1[-1]}")    # akses elemen terakhir
print(f"list1[len(list1) - 1]: {list1[len(list1) - 1]}")
  
  # A. Akses dengan jarak (Positif)  -> (0, 1, 2, ..., -1)
print(f"list1[2:]: {list1[2:]}")        # [x:]   -> x, x+1, x+2, ..., [-1] (index terakhir)
print(f"list2[:3]: {list2[:3]}")        # [:y]   -> [0], [1], [2], ..., y-1
print(f"list1[1:4]: {list1[1:4]}")      # [x:y]  -> x, x+1, x+2, ..., y-1

  # B. Akses dengan jarak (Negatif)  -> (..., -3, -2, -1)
print(f"list2[-2:]: {list2[-2:]}")      # [-x:]  -> -x, -x+1, -x+2, ..., [-1] (index terakhir)
print(f"list1[:-3]: {list1[:-3]}")      # [:-y]  -> [0], [1], [2],..., -y-1
print(f"list2[-4:-1]: {list2[-4:-1]}")  # [-x:-y]-> -x, -x+1, -x+2, ..., -y-1
print("-" * 40)

# 3. Mengubah Item
list3 = ["apple", "grape", 'pinapple', 'watermelon', 'banana', 'berry']
list3[2] = "avocado"
list3[-1] = "strawberry"
print(list3)

  # A. Menggunakan .insert
list3.insert(0, "mangga")   # .inser(index, value) -> akan menambah di indexnya dan item lainnya di sebelah kanan akan BERGESER
list3.insert(-1, "melon")
print(list3)
  # B. Menggunakan range
list3[3:] = ["semangka", "pisang", "stroberi"]
print(list3)
list3[1:3] = ["anggur"]     # Jika range index lebih banyak drpd item yg diganti, maka sisa item akan DIHAPUS dan item lainnya bergeser ke kiri
print(list3)
list3[3:5] = ["nangka", "leci", "ceri", "belimbing"]  # Jika range index lebih sedikit drpd item yg DIGANTI, maka sisa item akan ditambahkan di list ke kanan
print(list3)
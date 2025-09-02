# 1. .sort()  -> secara default alphanumerically, ascending
listStr = ["kambing", "ayam", "gajah", "kuda", "jerapah", "anjing"]
listNum = [4, 9, 1, 2, 9, 4, 7, 5]
# listMix = ["apple", 4, "tiga", 8.8, True, "sambal"]   error, gagal sort utk item beragam tipe data di list

listStr.sort()
listNum.sort()

print(listStr)
print(listNum)
  

# 2. Sort Descending, .sort(reverse = True)
list1 = ["b", "x", "q", "a", "j", "d"]
list1.sort(reverse= True)
print(list1)


# 3. Kostum Sort Function
def myFunc(n):
    return abs(n - 50)

list2 = [100, 75, 50, 25, 12, 5, 0]
list2.sort(key= myFunc)      # key-nya harus callable
print(list2)                 
# Hasil pengurangan:    50, 25, 0, 25, 38, 45, 50 
# Diurutkan:            0, 25, 25, 38, 45, 50, 50
# Item asli (hasil):    50, 75, 25, 12, 5, 100, 0


# 4. Case sensitive, upper dan lower case termasuk case sensitive  -> uppercase akan didahulukan
list3 = ["apel", "anggur", "ayam", "babi", "Belimbing", "Cicak", "Zebra"]
list3.sort()
print(list3)

  # gunakan key = str.lower()
list4 = ["apel", "anggur", "ayam", "babi", "Belimbing", "Cicak", "Zebra"]
list4.sort(key= str.lower)      # Tidak mengubah item asli ke lower
print(list4)


# 5. Reversed Order  -> tipe data mix di list dibolehkan
list5 = ["ayam", 3, 5, "coba", True, 9.9]
list5.reverse()
print(list5)
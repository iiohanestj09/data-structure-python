# 1. .sort()  -> secara default alphanumerically, ascending
listStr = ["kambing", "ayam", "gajah", "kuda", "jerapah", "anjing"]
listNum = [4, 9, 1, 2, 9, 4, 7, 5]
# listMix = ["apple", 4, "tiga", 8.8, True, "sambal"]   error, gagal sort utk item beragam tipe data di list

listStr.sort()
listNum.sort()

print(listStr)
print(listNum)
  
  # upper dan lower case termasuk case sensitive  -> uppercase akan didahulukan
list3 = ["apel", "anggur", "ayam", "babi", "Belimbing", "Cicak", "Zebra"]
list3.sort()
print(list3)


# 2. Sort Descending, .sort(reverse = True)
list1 = ["b", "x", "q", "a", "j", "d"]
list1.sort(reverse= True)
print(list1)


# 3. Kostum Sort Function
def myFunc(n):
    return abs(n - 50)

thisList = [100, 75, 50, 25, 12, 5, 0]
thisList.sort(key= myFunc)      # key-nya harus callable
print(thisList)                 
# Hasil pengurangan:    50, 25, 0, 25, 38, 45, 50 
# Diurutkan:            0, 25, 25, 38, 45, 50, 50
# Item asli (hasil):    50, 75, 25, 12, 5, 100, 0  
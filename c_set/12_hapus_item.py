# 1. .remove()
set1 = {"apple", "banana", "cherry", "manggo", "pinapple", "berry"}
set1.remove("banana")
# set1.remove("apalah")     Error, kalau remove item yg tidak ada, maka program akan error runtime
print(set1)


# 2. .pop()  -> hapus item secara RANDOM dan bisa mengembalikkan item yg dihapus
x = set1.pop()
print(x)
print(set1.pop())
print(set1)


# 3. .discard() -> jika item yg mau dihapus tidak ada, Tidak error
set1.discard("apple")   # bisa saja item "apple" sudah dihapus sebelumnya (di atas), bisa juga masih ada
print(set1)
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}

# 1. Iterasi Key
  # A. Secara manual
for x in dict1:
    print(x)
print()

  # B. Menggunakan .keys()
for key in dict1.keys():
    print(key)
print("-" * 20)


# 2. Iterasi Value
  # A. Secara manual
for x in dict1:
    print(dict1[x])
print()

  # B. Menggunakan .values()
for value in dict1.values():
    print(value)
print("-" * 20)


# 3. Iterasi Item (seluruh)
for key, value in dict1.items():
    print(f"{key}: {value}")
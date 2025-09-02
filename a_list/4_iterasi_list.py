list1 = [1, "anggur", False, "Dadang", True]

# 1. for in
for item in list1:
    print(item)
print("-" * 20)


# 2. for in dan range() untuk Index
for i in range(len(list1)):
    print(f"i: {i}, item: {list1[i]}")
print("-" * 20)


# 3. for in an enumerate()
for index,item in enumerate(list1):
    print(f"{index}, {item}")
print("-" * 20)


# 4. while
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print("-" * 20)


# 5. List Comperhension
[print(f"Item: {item}") for item in list1]
print("-" * 20)
[print(f"index: {i}, Item: {list1[i]}") for i in range(len(list1))]
print("-" * 20)
[print(f"{idx}, {itm}") for idx,itm in enumerate(list1)]
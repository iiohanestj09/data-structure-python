list1 = ["dudung", True, "tiga", 4.4, "upin", False]

# newList = [Expression for Item in List Condition]
# 1. List Comperhension
newList1 = [item for item in list1 if type(item) == type("")]
print(newList1)

  # jika tanpa condition  -> salin seluruhnya, karena semua kondisi bernilai True
newList2 = [item for item in list1]
print(newList2)
print("-" * 40)


# 2. Expression
newList3 = [str(x).upper() for x in list1]
print(newList3)

  # expression juga bisa ditambah dgn condition
newList4 = [x if x == "upin" else "bukanUpin" for x in list1]
print(newList4)
print("-" * 40)


# 3. Iterable
newList5 = [x for x in range(10)]
print(newList5)

  # jika ditambah condition
newList6 = [x for x in range(10) if x < 5]
print(newList6)

  # membuat list dengan nilai sama semua
newList7 = ["hello" for i in range(5)]
print(newList7)
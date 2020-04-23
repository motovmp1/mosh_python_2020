from sys import getsizeof

values = [x * 2 for x in range(10)]
for x in values:
    print(x, end=", ")

values1 = (x * 2 for x in range(10))
print(values1)
for x in values1:
    print(x, end=", ")

values3 = (x * 2 for x in range(10000))
print("gen:", getsizeof(values3))

values4 = [x * 2 for x in range(10000)]
print("gen:", getsizeof(values4))

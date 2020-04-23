numbers = [1, 1, 2, 3, 3, 4, 4]
uniques = set(numbers)
print(uniques)

second_bunch = {1, 3}
print(second_bunch)
print(len(second_bunch))
second_bunch.add(2)
print(second_bunch)
print(len(second_bunch))

numbers_second = [1, 1, 2, 3, 4]
first = set(numbers_second)
second = {1, 5}

print(first | second)

print(first & second)

print(first - second)

print(first ^ second)

if 1 in first:
    print("yes")



# cannot duplicated sets and cannot check by index

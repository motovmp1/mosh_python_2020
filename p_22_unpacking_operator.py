numbers = [1, 2, 3]
# unpacking operator is *
print(*numbers)

values = list(range(5))
print(*values)

text_range = [*range(5), *"hello"]
print(text_range)

first_list = [1, 2]
second_list = [3, 4]

values1 = [first_list, second_list]
print(values1)


values2 = [*first_list, "a", *second_list, *"hello"]
print(values2)

# can use dict also but ** need two 

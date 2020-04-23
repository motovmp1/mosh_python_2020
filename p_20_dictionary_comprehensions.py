values = []
for x in range(5):
    values.append(x * 2)
print(values)

# [expression for item in items]
# this is the same as above
values = [x * 2 for x in range(5)]
print(values)

# the same result for sets

values = {x * 2 for x in range(5)}
print(values)


point = {
    "x": 1,
    "y": 2

}
print(point)


point1 = dict(x=1, y=2)
print(point1)


print(point["x"])

if "an" in point1:
    print(point["a"])

print(point.get("a", 0))

for key in point:
    print(key, point[key])


for x in point.items():
    print(x)

for keys, value in point.items():
    print(keys, value)

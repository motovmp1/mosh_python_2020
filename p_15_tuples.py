"""

Tuples never change

(0)
"""

point = 1, 2
print(type(point))

point1 = (1, 2) + (3, 4)
print(point1)

point2 = (1, 2) * 3
print(point2)

point = tuple("hello world")
print(point[0:2])



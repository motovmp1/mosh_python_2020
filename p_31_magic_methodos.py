# class: blueprint for creating new objects
# Object : instance of class


class Point:
    color = "red"

    # this is a magic methods that they call __init__
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"


point = Point(1, 2)
print(point)
# class: blueprint for creating new objects
# Object : instance of class


class Point:
    color = "red"

    def __init__(self, x, y):
        self.x = y
        self.y = y

    # class is a decorator fro cls that allow to call you initial value.
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw_line(self):
        print(f"Point is: ({self.x}, {self.y})")
        return 1


# This is a class that I can call
Point.color = "yellow"

# here you can start your point when you call cls
point = Point.zero()

print(point.draw_line())


print(point.color)


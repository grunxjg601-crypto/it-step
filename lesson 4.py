class Shape:
    def __init__(self, color="black"):
        self.color = color

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, color="black", width=0, height=0):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color="black", radius=0):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rectangle = Rectangle("red", 5, 10)
circle = Circle("blue", 4)

print("Прямокутник:")
print("Колір:", rectangle.color)
print("Ширина:", rectangle.width)
print("Висота:", rectangle.height)
print("Площа:", rectangle.area())

print("Коло:")
print("Колір:", circle.color)
print("Радіус:", circle.radius)
print("Площа:", circle.area())

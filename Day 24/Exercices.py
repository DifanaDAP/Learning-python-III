# Day 24: Polymorphism & Abstract Class

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1415 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * self.a * self.height

    def perimeter(self):
        return self.a + self.b + self.c

# Polymorphism in action
def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Print areas of all shapes in a list
def print_all_areas(shapes):
    for i, shape in enumerate(shapes, start=1):
        print(f"Shape {i} area: {shape.area()}")

# Testing
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 2.5)

print("--- Circle ---")
print_shape_info(circle)

print("\n--- Rectangle ---")
print_shape_info(rectangle)

print("\n--- Triangle ---")
print_shape_info(triangle)

print("\n--- All Areas ---")
shapes = [circle, rectangle, triangle]
print_all_areas(shapes)

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

# Polymorphism in action
def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("--- Circle ---")
print_shape_info(circle)

print("\n--- Rectangle ---")
print_shape_info(rectangle)

# Exercises:
# 1. Create a new shape class called Triangle with area and perimeter methods.
# 2. Add another function that accepts a list of shapes and prints all their areas.

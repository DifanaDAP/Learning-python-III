# day 22 Introducion to OOP - Class & object

#defining a simple class
class Person:
    def __init__(self, Name, age):
        self.name = Name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old")

# creating object
person1 = Person("Alice", 24)
person2 = Person("Jack", 30)

# call menthod
person1.greet()
person2.greet()

# Exercises:
# 1. Create another class called "Car" with attributes: brand, model, and year.
# 2. Add a method called "description" that prints the car's details.
# 3. Create 2 car objects and call their description methods.
# DAy 25 : Design Pattern - Singleton & factory

# sigleton Pattern
class singleton:
    _intance = None

    def __new__(cls):
        if cls._intance is None:
            print("Creating a new Instance")
            cls._intance = super(singleton, cls).__new__(cls)
        else:
            print("Using excisting instance")
        return cls._intance
    
# factoru pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown Animal Type")
    
# testing singleton
print("--- Singleton Test ---")
a = singleton()
b = singleton()
print(f"a is b: {a is b}")

# Testing Factory
print("\n--- Factory Test ---")
animal1 = AnimalFactory.create_animal("dog")
animal2 = AnimalFactory.create_animal("cat")
print(f"Animal 1 Says: {animal1.speak()}")
print(f"Animal 2 Says: {animal2.speak()}")

# Exercises:
# 1. Modify Singleton to store a value and print it when accessed.
# 2. Extend the factory to create a Bird class with a speak method.
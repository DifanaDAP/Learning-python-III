# Exercises:
# 1. Create another class called "Car" with attributes: brand, model, and year.
class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def greet(self):
        print(f"Brand car {self.brand}, the model{self.model}, the production {self.year}")

# 2. Add a method called "description" that prints the car's details.
description1 = car("Mitsubitshi", "Xpander", 2022)
description2 = car("Lamborgini", "Urakan", 2016)

# 3. Create 2 car objects and call their description methods.
description1.greet()
description2.greet()
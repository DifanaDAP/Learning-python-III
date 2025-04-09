# Day 23 Encapsulation & inheritance

# Encapsulation Example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # private atribut

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. new balance: ${self.__balance}")
        else:
            print("Insufficient Funds")

    def get_balance(self):
        return self.__balance
    
# Inherintance Example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} make a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} backs")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


# testing the class
print("--- Bank Account Test ---")
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: ${account.get_balance()}")

print("\n--- Inheritance Test ---")
dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()
cat.speak()


# Exercises:
# 1. Create a subclass of BankAccount called SavingsAccount that adds interest.
# 2. Create another animal class, like Bird, and override the speak method.
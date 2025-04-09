# Exercises:
# 1. Create a subclass of BankAccount called SavingsAccount that adds interest.
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

#subclass of BankAccount
class SavingAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} added.")
    

# 2. Create another animal class, like Bird, and override the speak method.
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

class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps")


# testing the class
print("--- Bank Account Test ---")
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: ${account.get_balance()}")

print("\n--- Savings Account ---")
savings = SavingAccount("Bob", 200, 0.05)
savings.add_interest()
print(f"Balance after interest: ${savings.get_balance()}")

print("\n--- Inheritance Test ---")
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")
dog.speak()
cat.speak()
bird.speak()


# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Derived class (Child) inherits from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

# --- How to use it ---

# 1. Create an instance of the child class
my_dog = Dog(name="Buddy")

# 2. Access the inherited method from the parent class
print(my_dog.eat())   # Output: Buddy is eating.

# 3. Access the unique method belonging to the child class
print(my_dog.bark())  # Output: Buddy says Woof!

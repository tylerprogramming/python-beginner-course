# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object
person1 = Person("Alice", 30)
print("Name:", person1.name)  # Output: Name: Alice
print("Age:", person1.age)  # Output: Age: 30


# Adding methods to a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Creating an object and calling a method
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

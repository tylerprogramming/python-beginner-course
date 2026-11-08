# Python Beginner's Tutorial

Welcome to the Python Beginner's Tutorial! This guide will take you from the basics of Python programming to working with databases. Here's a breakdown of what you'll learn:

### Lesson files

The folder numbers do not match the section numbers below (two folders share `06`). Use this map:

| Section | Folder / file |
|---|---|
| 4. Variables and Data Types | `01 - variables and data types/main.py` |
| 4. Basic Operations | `02 - basic operations/main.py` |
| 4. Strings | `03 - strings/main.py` |
| 5. Control Flow | `04 - conditional statements/ifelse.py`, `loops.py` |
| 6. Lists | `05 - lists/lists.py` |
| 6. Tuples, Dictionaries | `06 - tuples/tuples.py`, `dictionary.py` |
| 6. Sets | no lesson file yet |
| 7. Functions | `06 - functions/def.py` |
| 8. Modules and Packages | `07 - modules and packages/modpack.py` |
| 9. File Handling | `08 - file handling/file.py` |
| 10. Exception Handling | `09 - exception handling/exception.py` |
| 11. OOP | `10 - OOP/oop.py` |
| 12. Databases (SQLite) | `12 - sqlite/main.py` |
| 13. Project (contact book) | `11 - project/main.py` |

Every lesson uses only the standard library.

## 1. Introduction
Python is a high-level, interpreted programming language known for its readability and simplicity. It's widely used for web development, data analysis, artificial intelligence, scientific computing, and automation.
```python
print("Hello, World!")
```

## 2. Installing Python
1. Download the latest version for your operating system from [python.org](https://www.python.org/downloads/).
2. Run the installer. On Windows, check "Add Python to PATH".
3. Verify the installation with `python3 --version` (or `python --version` on Windows).

## 3. Setting Up a Development Environment
Use a code editor or IDE such as VS Code or PyCharm. For VS Code:

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the Python extension from the VS Code marketplace.
3. Open this folder and run any lesson file with the Run button, or from a terminal:

```bash
python3 "01 - variables and data types/main.py"
```

## 4. Basic Syntax and Operations

### Variables and Data Types
Understand how to use variables and data types.

```python
name = "Alice"
age = 25
```

### Basic Operations
Perform arithmetic, comparison, and logical operations.

```python
result = 10 + 5
is_greater = 10 > 5
```

## 5. Control Flow

### Conditional Statements
Make decisions in your code using `if`, `else`, and `elif`.

```python
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Loops
Repeat actions with `for` and `while` loops.

```python
for i in range(5):
    print(i)
```

## 6. Data Structures

### Lists
Store and manipulate collections of items.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
```

### Tuples
Work with immutable sequences.

```python
dimensions = (1920, 1080)
```

### Dictionaries
Store key-value pairs.

```python
person = {"name": "Alice", "age": 25}
```

### Sets
Store unique items and perform set operations.

```python
unique_numbers = {1, 2, 3, 4, 4, 5}
```

## 7. Functions

### Defining Functions
Create reusable blocks of code.

```python
def greet(name):
    return f"Hello, {name}!"
```

### Function Arguments and Return Values
Pass data to functions and get results back.

```python
message = greet("Alice")
```

## 8. Modules and Packages

### Importing Modules
Use Python’s built-in modules.

```python
import math
print(math.sqrt(16))
```

### Using Standard Library Modules
Explore common modules from the standard library.

```python
import random
print(random.randint(1, 10))
```

## 9. File Handling

### Reading from and Writing to Files
Interact with files in Python.

```python
with open('example.txt', 'w') as f:
    f.write("Hello, file!")
```

## 10. Exception Handling

### Try, Except Blocks
Handle errors gracefully.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 11. Introduction to Object-Oriented Programming (OOP)

### Classes and Objects
Create classes and objects to model real-world entities.

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Rex")
```

### Methods and Attributes
Define behaviors and properties for your classes.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Rex")
print(dog.bark())
```

## 12. Databases: Interacting with SQLite and SQLAlchemy

### Using SQLite
Create and interact with a simple SQLite database.

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()
conn.close()
```

### Using SQLAlchemy
Use SQLAlchemy ORM to interact with databases.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
```

## 13. Project: Bringing It All Together
Apply what you've learned by building a simple project that ties together the concepts of variables, control flow, data structures, functions, file handling, and database interaction.

```python
# Example project snippet
user_data = {"name": "Alice", "age": 25}
if user_data['age'] > 18:
    print(f"{user_data['name']} is an adult.")
```

---

By the end of this tutorial, you'll have a solid understanding of Python and the skills to start building your own projects. Happy coding!
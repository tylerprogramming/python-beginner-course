# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print("Name:", person["name"])  # Output: Alice

# Modifying values
person["age"] = 26
print("Modified dictionary:", person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Adding key-value pairs
person["email"] = "alice@example.com"
print("Dictionary with new key-value pair:", person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Removing key-value pairs
del person["city"]
print("Dictionary after deletion:", person)  # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
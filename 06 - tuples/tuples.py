# Tuples
fruit_tuple = ("apple", "banana", "cherry")

# Accessing elements
print("First fruit:", fruit_tuple[0])  # Output: apple

# Tuples are immutable, so elements cannot be changed or added
# But you can concatenate tuples
new_fruit_tuple = fruit_tuple + ("date",)
print("Concatenated tuple:", new_fruit_tuple)  # Output: ('apple', 'banana', 'cherry', 'date')
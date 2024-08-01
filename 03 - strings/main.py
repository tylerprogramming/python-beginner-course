# Strings
greeting = "Hello"
name = "Alice"

# Concatenation
message = greeting + ", " + name + "!"
print("Concatenated string:", message)  # Output: Hello, Alice!

# String methods
print("Uppercase:", message.upper())   # Output: HELLO, ALICE!
print("Lowercase:", message.lower())   # Output: hello, alice!
print("Replace:", message.replace("Alice", "Bob")) # Output: Hello, Bob!

# String slicing
print("Slice [0:5]:", message[0:5])    # Output: Hello
print("Slice [7:]:", message[7:])      # Output: Alice!
print("Last character:", message[-1])  # Output: !
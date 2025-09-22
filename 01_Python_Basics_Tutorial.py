
# test pull request 
=======

# Python Basics Tutorial for Beginners
# This file contains comprehensive examples of Python fundamentals
#
print("=" * 50)
print("PYTHON BASICS TUTORIAL")
print("=" * 50)

# =============================================================================
# 1. VARIABLES AND DATA TYPES
# =============================================================================

print("\n1. VARIABLES AND DATA TYPES")
print("-" * 30)

# Variables in Python
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Is Student: {is_student} (Type: {type(is_student)})")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# =============================================================================
# 2. STRING OPERATIONS
# =============================================================================

print("\n2. STRING OPERATIONS")
print("-" * 30)

# String methods
text = "Hello, World!"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('World', 'Python')}")

# String formatting
name = "Bob"
age = 30
print(f"Hello, {name}! You are {age} years old.")
print("Hello, {}! You are {} years old.".format(name, age))

# =============================================================================
# 3. NUMBERS AND MATH OPERATIONS
# =============================================================================

print("\n3. NUMBERS AND MATH OPERATIONS")
print("-" * 30)

# Basic arithmetic
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Math functions
import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Absolute value of -5: {abs(-5)}")
print(f"Round 3.7: {round(3.7)}")

# =============================================================================
# 4. LISTS
# =============================================================================

print("\n4. LISTS")
print("-" * 30)

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# List operations
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Fruits length: {len(fruits)}")

# Adding elements
fruits.append("grape")
print(f"After append: {fruits}")

fruits.insert(1, "mango")
print(f"After insert: {fruits}")

# Removing elements
fruits.remove("banana")
print(f"After remove: {fruits}")

popped = fruits.pop()
print(f"Popped: {popped}, Remaining: {fruits}")

# =============================================================================
# 5. TUPLES
# =============================================================================

print("\n5. TUPLES")
print("-" * 30)

# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single item tuple

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single item: {single_item}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# =============================================================================
# 6. DICTIONARIES
# =============================================================================

print("\n6. DICTIONARIES")
print("-" * 30)

# Creating dictionaries
person = {
    "name": "Charlie",
    "age": 28,
    "city": "New York",
    "is_employed": True
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age', 'Not specified')}")

# Adding/updating values
person["occupation"] = "Engineer"
person["age"] = 29
print(f"Updated person: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# =============================================================================
# 7. SETS
# =============================================================================

print("\n7. SETS")
print("-" * 30)

# Creating sets
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "orange", "apple"}  # Duplicates removed

print(f"Numbers set: {numbers_set}")
print(f"Fruits set: {fruits_set}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# =============================================================================
# 8. INPUT AND OUTPUT
# =============================================================================

print("\n8. INPUT AND OUTPUT")
print("-" * 30)

# Getting user input (commented out for tutorial)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you are {age} years old!")

# File operations
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\nThis is a sample file.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# =============================================================================
# 9. TYPE CONVERSION
# =============================================================================

print("\n9. TYPE CONVERSION")
print("-" * 30)

# Converting between types
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"String: '{num_str}' (Type: {type(num_str)})")
print(f"Integer: {num_int} (Type: {type(num_int)})")
print(f"Float: {num_float} (Type: {type(num_float)})")

# Converting to string
number = 42
text = str(number)
print(f"Number to string: '{text}' (Type: {type(text)})")

# =============================================================================
# 10. COMMENTS AND DOCSTRINGS
# =============================================================================

print("\n10. COMMENTS AND DOCSTRINGS")
print("-" * 30)

# Single line comment
# This is a single line comment

"""
This is a multi-line comment
or docstring
"""

def example_function():
    """
    This is a docstring that describes what the function does.
    It's a good practice to document your functions.
    """
    return "This function returns a string"

print(f"Function result: {example_function()}")

print("\n" + "=" * 50)
print("END OF PYTHON BASICS TUTORIAL")
print("=" * 50)

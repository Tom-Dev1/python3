# Functions and Modules Tutorial for Beginners
# This file covers function definition, parameters, return values, and modules

print("=" * 60)
print("PYTHON FUNCTIONS AND MODULES TUTORIAL")
print("=" * 60)

# =============================================================================
# 1. FUNCTION BASICS
# =============================================================================

print("\n1. FUNCTION BASICS")
print("-" * 40)

# Simple function without parameters
def greet():
    """A simple greeting function"""
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

# Function with multiple parameters
def greet_with_age(name, age):
    """Greet person with their age"""
    print(f"Hello, {name}! You are {age} years old.")

# Function with return value
def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

# Function with multiple return values
def get_name_and_age():
    """Return multiple values"""
    return "Alice", 25

# Testing basic functions
greet()
greet_person("Bob")
greet_with_age("Charlie", 30)

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# =============================================================================
# 2. PARAMETER TYPES
# =============================================================================

print("\n2. PARAMETER TYPES")
print("-" * 40)

# Default parameters
def greet_with_default(name, greeting="Hello"):
    """Function with default parameter"""
    print(f"{greeting}, {name}!")

greet_with_default("Alice")
greet_with_default("Bob", "Hi")

# Keyword arguments
def create_profile(name, age, city, occupation="Student"):
    """Function with keyword arguments"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Occupation: {occupation}")

# Using keyword arguments
create_profile(name="David", age=28, city="Boston")
create_profile("Eve", 22, "Chicago", occupation="Engineer")

# Variable-length arguments (*args)
def sum_all(*numbers):
    """Sum all provided numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# Keyword arguments (**kwargs)
def print_info(**kwargs):
    """Print information using keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Frank", age=35, city="Seattle")

# =============================================================================
# 3. LAMBDA FUNCTIONS
# =============================================================================

print("\n3. LAMBDA FUNCTIONS")
print("-" * 40)

# Basic lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"Add 3 and 4: {add(3, 4)}")

# Lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Lambda with sorted
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students sorted by grade: {sorted_by_grade}")

# =============================================================================
# 4. SCOPE AND NAMESPACE
# =============================================================================

print("\n4. SCOPE AND NAMESPACE")
print("-" * 40)

# Global and local variables
global_var = "I'm global"

def scope_demo():
    """Demonstrate variable scope"""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variables
counter = 0

def increment_counter():
    """Increment global counter"""
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment_counter()
increment_counter()

# =============================================================================
# 5. RECURSION
# =============================================================================

print("\n5. RECURSION")
print("-" * 40)

# Factorial using recursion
def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Fibonacci sequence using recursion
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# =============================================================================
# 6. MODULES AND PACKAGES
# =============================================================================

print("\n6. MODULES AND PACKAGES")
print("-" * 40)

# Importing built-in modules
import math
import random
import datetime

# Using math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")

# Using random module
print(f"Random number: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")

# Using datetime module
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Current date: {now.date()}")

# Import specific functions
from math import sqrt, pow
print(f"Square root using import: {sqrt(25)}")
print(f"Power using import: {pow(2, 3)}")

# Import with alias
import datetime as dt
print(f"Current year: {dt.datetime.now().year}")

# =============================================================================
# 7. CREATING CUSTOM MODULES
# =============================================================================

print("\n7. CREATING CUSTOM MODULES")
print("-" * 40)

# Let's create a simple math utilities module
def create_math_utils():
    """Create a simple math utilities module content"""
    math_utils_content = '''
# math_utils.py - Custom math utilities module

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def is_odd(number):
    """Check if a number is odd"""
    return number % 2 != 0

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Constants
PI = 3.14159
E = 2.71828
'''
    return math_utils_content

# Write the module to a file
with open("math_utils.py", "w") as f:
    f.write(create_math_utils())

# Import our custom module
import math_utils

# Use functions from our custom module
print(f"Is 7 even? {math_utils.is_even(7)}")
print(f"Is 8 even? {math_utils.is_even(8)}")
print(f"Is 17 prime? {math_utils.is_prime(17)}")
print(f"Factorial of 6: {math_utils.factorial(6)}")
print(f"PI from our module: {math_utils.PI}")

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("\n8. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Calculator functions
def calculator():
    """Simple calculator using functions"""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    
    # Test calculator
    print("Calculator Demo:")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"10 / 0 = {divide(10, 0)}")

calculator()

# Example 2: Text processing functions
def text_processor():
    """Text processing utility functions"""
    
    def count_words(text):
        """Count words in text"""
        return len(text.split())
    
    def count_characters(text):
        """Count characters in text"""
        return len(text)
    
    def reverse_text(text):
        """Reverse the text"""
        return text[::-1]
    
    def capitalize_words(text):
        """Capitalize each word"""
        return ' '.join(word.capitalize() for word in text.split())
    
    # Test text processor
    sample_text = "hello world python programming"
    print(f"\nText: '{sample_text}'")
    print(f"Word count: {count_words(sample_text)}")
    print(f"Character count: {count_characters(sample_text)}")
    print(f"Reversed: '{reverse_text(sample_text)}'")
    print(f"Capitalized: '{capitalize_words(sample_text)}'")

text_processor()

# Example 3: Data validation functions
def data_validator():
    """Data validation utility functions"""
    
    def is_valid_email(email):
        """Basic email validation"""
        return "@" in email and "." in email.split("@")[1]
    
    def is_valid_age(age):
        """Validate age"""
        try:
            age_num = int(age)
            return 0 <= age_num <= 150
        except ValueError:
            return False
    
    def is_valid_phone(phone):
        """Basic phone validation"""
        # Remove non-digits
        digits = ''.join(filter(str.isdigit, phone))
        return len(digits) == 10
    
    # Test validator
    print("\nData Validation Demo:")
    print(f"Email 'test@example.com' valid: {is_valid_email('test@example.com')}")
    print(f"Email 'invalid-email' valid: {is_valid_email('invalid-email')}")
    print(f"Age '25' valid: {is_valid_age('25')}")
    print(f"Age 'abc' valid: {is_valid_age('abc')}")
    print(f"Phone '123-456-7890' valid: {is_valid_phone('123-456-7890')}")
    print(f"Phone '123' valid: {is_valid_phone('123')}")

data_validator()

# =============================================================================
# 9. FUNCTION DECORATORS (INTRODUCTION)
# =============================================================================

print("\n9. FUNCTION DECORATORS (INTRODUCTION)")
print("-" * 40)

# Simple decorator example
def timing_decorator(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Using the decorator
@timing_decorator
def slow_function():
    """A function that takes some time"""
    import time
    time.sleep(0.1)  # Simulate work
    return "Done!"

result = slow_function()
print(f"Result: {result}")

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n10. BEST PRACTICES")
print("-" * 40)

# 1. Use descriptive function names
def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

# 2. Use docstrings
def find_maximum(numbers):
    """
    Find the maximum number in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: Maximum number in the list
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum

# 3. Handle errors gracefully
def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"

# Test best practices
print(f"Circle area (radius=5): {calculate_circle_area(5):.2f}")
print(f"Maximum of [1,5,3,9,2]: {find_maximum([1,5,3,9,2])}")
print(f"Safe divide 10/2: {safe_divide(10, 2)}")
print(f"Safe divide 10/0: {safe_divide(10, 0)}")

print("\n" + "=" * 60)
print("END OF FUNCTIONS AND MODULES TUTORIAL")
print("=" * 60)

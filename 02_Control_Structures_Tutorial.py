# Testing 1111
# Control Structures Tutorial for Beginners
# This file covers conditional statements, loops, and control flow

print("=" * 60)
print("PYTHON CONTROL STRUCTURES TUTORIAL")
print("=" * 60)

# =============================================================================
# 1. CONDITIONAL STATEMENTS (if, elif, else)
# =============================================================================

print("\n1. CONDITIONAL STATEMENTS")
print("-" * 40)

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement
score = 85
if score >= 60:
    print("You passed!")
else:
    print("You failed!")

# if-elif-else statement
grade = 87
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Multiple conditions
temperature = 25
humidity = 60

if temperature > 30 and humidity > 70:
    print("It's hot and humid!")
elif temperature > 30 or humidity > 70:
    print("It's either hot or humid!")
else:
    print("Weather is comfortable!")

# Nested conditions
user_age = 25
has_license = True

if user_age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive!")
else:
    print("You're too young to drive!")

# =============================================================================
# 2. LOOPS - FOR LOOPS
# =============================================================================

print("\n2. FOR LOOPS")
print("-" * 40)

# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# For loop with step
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(f"Even: {i}")

# For loop with list
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in the list:")
for fruit in fruits:
    print(f"- {fruit}")

# For loop with enumerate (get index and value)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# For loop with dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("\nPerson details:")
for key, value in person.items():
    print(f"{key}: {value}")

# Nested for loops
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# =============================================================================
# 3. LOOPS - WHILE LOOPS
# =============================================================================

print("\n3. WHILE LOOPS")
print("-" * 40)

# Basic while loop
count = 1
print("Counting with while loop:")
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input simulation
# (commented out for tutorial)
"""
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
"""

# While loop with break
number = 1
print("\nNumbers until we reach 5:")
while True:
    print(f"Number: {number}")
    number += 1
    if number > 5:
        break

# =============================================================================
# 4. BREAK AND CONTINUE STATEMENTS
# =============================================================================

print("\n4. BREAK AND CONTINUE")
print("-" * 40)

# Break statement
print("Numbers 1-10, stopping at 5:")
for i in range(1, 11):
    if i == 6:
        break
    print(f"Number: {i}")

# Continue statement
print("\nEven numbers from 1-10:")
for i in range(1, 11):
    if i % 2 != 0:  # Skip odd numbers
        continue
    print(f"Even: {i}")

# Break in nested loops
print("\nBreaking out of nested loop:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print("Breaking at (1,1)")
            break
        print(f"({i}, {j})")
    else:
        continue  # Only executed if inner loop didn't break
    break  # Break outer loop if inner loop broke

# =============================================================================
# 5. LIST COMPREHENSIONS
# =============================================================================

print("\n5. LIST COMPREHENSIONS")
print("-" * 40)

# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# List comprehension with string manipulation
words = ["hello", "world", "python", "programming"]
upper_words = [word.upper() for word in words]
print(f"Upper words: {upper_words}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# =============================================================================
# 6. PRACTICAL EXAMPLES
# =============================================================================

print("\n6. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Number guessing game logic
def number_guessing_game():
    """Simulate a number guessing game"""
    secret_number = 7
    attempts = 0
    max_attempts = 3
    
    print("Guess the number between 1 and 10!")
    
    while attempts < max_attempts:
        # In real game: guess = int(input("Enter your guess: "))
        guess = 5  # Simulated guess
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Game over! The number was {secret_number}")
    return False

# Example 2: Grade calculator
def calculate_grade(score):
    """Calculate letter grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test grade calculator
scores = [95, 87, 73, 65, 45]
print("Grade calculations:")
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score} -> Grade: {grade}")

# Example 3: Prime number checker
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find prime numbers in range
print("\nPrime numbers from 1 to 20:")
primes = [num for num in range(1, 21) if is_prime(num)]
print(f"Primes: {primes}")

# Example 4: Text processing
def count_vowels(text):
    """Count vowels in a text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "Hello, Python Programming!"
vowel_count = count_vowels(text)
print(f"\nText: '{text}'")
print(f"Number of vowels: {vowel_count}")

# =============================================================================
# 7. COMMON PATTERNS AND BEST PRACTICES
# =============================================================================

print("\n7. COMMON PATTERNS AND BEST PRACTICES")
print("-" * 40)

# Pattern 1: Input validation loop
def get_positive_number():
    """Get a positive number from user"""
    while True:
        try:
            # In real code: num = float(input("Enter a positive number: "))
            num = 5.5  # Simulated input
            if num > 0:
                return num
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

# Pattern 2: Menu-driven program structure
def show_menu():
    """Display menu options"""
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

def menu_demo():
    """Demonstrate menu structure"""
    while True:
        show_menu()
        # In real code: choice = input("Enter your choice: ")
        choice = "3"  # Simulated choice to exit
        
        if choice == "1":
            print("You selected Option 1")
        elif choice == "2":
            print("You selected Option 2")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Pattern 3: Data processing with loops
def process_scores():
    """Process a list of scores"""
    scores = [85, 92, 78, 96, 88, 91]
    
    # Calculate statistics
    total = 0
    highest = scores[0]
    lowest = scores[0]
    
    for score in scores:
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    average = total / len(scores)
    
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

process_scores()

print("\n" + "=" * 60)
print("END OF CONTROL STRUCTURES TUTORIAL")
print("=" * 60)

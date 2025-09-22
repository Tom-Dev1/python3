# testttt2
# Object-Oriented Programming Tutorial for Beginners
# This file covers classes, objects, inheritance, and polymorphism
# Test 2
print("=" * 60)
print("PYTHON OBJECT-ORIENTED PROGRAMMING TUTORIAL")
print("=" * 60)

# =============================================================================
# 1. CLASSES AND OBJECTS BASICS
# =============================================================================

print("\n1. CLASSES AND OBJECTS BASICS")
print("-" * 40)

# Simple class definition
class Dog:
    """A simple Dog class"""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a new Dog instance"""
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def describe(self):
        """Describe the dog"""
        return f"{self.name} is {self.age} years old and is a {self.species}"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Using objects
print(dog1.bark())
print(dog2.describe())
print(f"Species: {Dog.species}")

# =============================================================================
# 2. CONSTRUCTORS AND DESTRUCTORS
# =============================================================================

print("\n2. CONSTRUCTORS AND DESTRUCTORS")
print("-" * 40)

class Person:
    """A Person class with constructor and destructor"""
    
    def __init__(self, name, age):
        """Constructor - called when object is created"""
        self.name = name
        self.age = age
        print(f"Person {self.name} created")
    
    def __del__(self):
        """Destructor - called when object is destroyed"""
        print(f"Person {self.name} destroyed")
    
    def introduce(self):
        """Introduce the person"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Creating and using person objects
person1 = Person("Alice", 25)
print(person1.introduce())

# The destructor will be called when the object goes out of scope
del person1

# =============================================================================
# 3. INSTANCE METHODS, CLASS METHODS, AND STATIC METHODS
# =============================================================================

print("\n3. INSTANCE, CLASS, AND STATIC METHODS")
print("-" * 40)

class Circle:
    """A Circle class demonstrating different method types"""
    
    # Class attribute
    pi = 3.14159
    
    def __init__(self, radius):
        """Constructor"""
        self.radius = radius
    
    # Instance method (needs self)
    def area(self):
        """Calculate area of the circle"""
        return self.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference of the circle"""
        return 2 * self.pi * self.radius
    
    # Class method (needs cls)
    @classmethod
    def from_diameter(cls, diameter):
        """Create circle from diameter"""
        return cls(diameter / 2)
    
    @classmethod
    def set_pi(cls, new_pi):
        """Set the value of pi for all circles"""
        cls.pi = new_pi
    
    # Static method (doesn't need self or cls)
    @staticmethod
    def is_valid_radius(radius):
        """Check if radius is valid"""
        return radius > 0

# Using different method types
circle1 = Circle(5)
print(f"Circle area: {circle1.area():.2f}")
print(f"Circle circumference: {circle1.circumference():.2f}")

# Class method
circle2 = Circle.from_diameter(10)
print(f"Circle from diameter: radius={circle2.radius}")

# Static method
print(f"Is radius 5 valid? {Circle.is_valid_radius(5)}")
print(f"Is radius -3 valid? {Circle.is_valid_radius(-3)}")

# =============================================================================
# 4. ENCAPSULATION - PRIVATE AND PROTECTED ATTRIBUTES
# =============================================================================

print("\n4. ENCAPSULATION")
print("-" * 40)

class BankAccount:
    """A BankAccount class demonstrating encapsulation"""
    
    def __init__(self, account_number, initial_balance=0):
        """Initialize bank account"""
        self.account_number = account_number
        self._balance = initial_balance  # Protected attribute (convention)
        self.__pin = "1234"  # Private attribute (name mangling)
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        """Withdraw money from account"""
        if pin != self.__pin:
            return "Invalid PIN"
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        """Get current balance"""
        return self._balance
    
    def change_pin(self, old_pin, new_pin):
        """Change PIN"""
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "PIN changed successfully"
        else:
            return "Invalid old PIN"

# Using encapsulation
account = BankAccount("12345", 1000)
print(account.deposit(500))
print(account.withdraw(200, "1234"))
print(f"Current balance: ${account.get_balance()}")
print(account.change_pin("1234", "5678"))

# =============================================================================
# 5. INHERITANCE
# =============================================================================

print("\n5. INHERITANCE")
print("-" * 40)

# Parent class
class Animal:
    """Base Animal class"""
    
    def __init__(self, name, species):
        """Initialize animal"""
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Make a generic animal sound"""
        return f"{self.name} makes a sound"
    
    def move(self):
        """Generic movement"""
        return f"{self.name} moves"
    
    def describe(self):
        """Describe the animal"""
        return f"{self.name} is a {self.species}"

# Child class
class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        """Initialize dog"""
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} barks: Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} fetches the ball"

# Another child class
class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, color):
        """Initialize cat"""
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} meows: Meow!"
    
    def climb(self):
        """Cat-specific method"""
        return f"{self.name} climbs the tree"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.describe())
print(dog.make_sound())
print(dog.fetch())

print(cat.describe())
print(cat.make_sound())
print(cat.climb())

# =============================================================================
# 6. MULTIPLE INHERITANCE
# =============================================================================

print("\n6. MULTIPLE INHERITANCE")
print("-" * 40)

class Flyable:
    """Mixin class for flying ability"""
    
    def fly(self):
        """Fly method"""
        return f"{self.name} is flying"

class Swimmable:
    """Mixin class for swimming ability"""
    
    def swim(self):
        """Swim method"""
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance"""
    
    def __init__(self, name):
        """Initialize duck"""
        super().__init__(name, "Duck")
    
    def make_sound(self):
        """Override make_sound"""
        return f"{self.name} quacks: Quack!"

# Using multiple inheritance
duck = Duck("Donald")
print(duck.describe())
print(duck.make_sound())
print(duck.fly())
print(duck.swim())

# =============================================================================
# 7. POLYMORPHISM
# =============================================================================

print("\n7. POLYMORPHISM")
print("-" * 40)

# Polymorphism with inheritance
def animal_sounds(animals):
    """Demonstrate polymorphism"""
    for animal in animals:
        print(animal.make_sound())

# Create different animals
animals = [
    Dog("Rex", "German Shepherd"),
    Cat("Fluffy", "White"),
    Duck("Daffy")
]

print("Animal sounds:")
animal_sounds(animals)

# Polymorphism with duck typing
class Car:
    """Car class"""
    
    def start(self):
        return "Car engine started"
    
    def stop(self):
        return "Car engine stopped"

class Bicycle:
    """Bicycle class"""
    
    def start(self):
        return "Bicycle pedaling started"
    
    def stop(self):
        return "Bicycle stopped"

def operate_vehicle(vehicle):
    """Operate any vehicle (duck typing)"""
    print(vehicle.start())
    print(vehicle.stop())

# Using duck typing
car = Car()
bike = Bicycle()

print("\nOperating vehicles:")
operate_vehicle(car)
operate_vehicle(bike)

# =============================================================================
# 8. SPECIAL METHODS (MAGIC METHODS)
# =============================================================================

print("\n8. SPECIAL METHODS (MAGIC METHODS)")
print("-" * 40)

class Book:
    """Book class with special methods"""
    
    def __init__(self, title, author, pages):
        """Constructor"""
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Developer representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of book (pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Book):
            return (self.title == other.title and 
                   self.author == other.author)
        return False
    
    def __add__(self, other):
        """Add two books (combine pages)"""
        if isinstance(other, Book):
            return Book(
                f"{self.title} & {other.title}",
                f"{self.author} & {other.author}",
                self.pages + other.pages
            )
        return NotImplemented

# Using special methods
book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 400)

print(f"Book 1: {book1}")
print(f"Book 1 repr: {repr(book1)}")
print(f"Book 1 length: {len(book1)} pages")

book3 = Book("Python Basics", "John Doe", 250)
print(f"Book 1 == Book 3: {book1 == book3}")

combined_book = book1 + book2
print(f"Combined book: {combined_book}")
print(f"Combined pages: {len(combined_book)}")

# =============================================================================
# 9. PROPERTIES AND GETTERS/SETTERS
# =============================================================================

print("\n9. PROPERTIES AND GETTERS/SETTERS")
print("-" * 40)

class Temperature:
    """Temperature class with properties"""
    
    def __init__(self, celsius=0):
        """Initialize temperature"""
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.celsius = (value - 32) * 5/9

# Using properties
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

# =============================================================================
# 10. PRACTICAL EXAMPLES
# =============================================================================

print("\n10. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Library Management System
class Book:
    """Book class for library system"""
    
    def __init__(self, isbn, title, author, year):
        """Initialize book"""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
    
    def __str__(self):
        """String representation"""
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"

class Library:
    """Library class"""
    
    def __init__(self, name):
        """Initialize library"""
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """Add book to library"""
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def find_book(self, title):
        """Find book by title"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def borrow_book(self, title):
        """Borrow a book"""
        book = self.find_book(title)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return f"Borrowed: {book.title}"
        elif book and book.is_borrowed:
            return f"Book '{title}' is already borrowed"
        else:
            return f"Book '{title}' not found"
    
    def return_book(self, title):
        """Return a book"""
        book = self.find_book(title)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return f"Returned: {book.title}"
        elif book and not book.is_borrowed:
            return f"Book '{title}' is not borrowed"
        else:
            return f"Book '{title}' not found"
    
    def list_books(self):
        """List all books"""
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            print(f"  {book}")

# Using the library system
library = Library("City Library")

# Add books
book1 = Book("123456", "Python Programming", "Alice Johnson", 2023)
book2 = Book("789012", "Data Structures", "Bob Smith", 2022)
book3 = Book("345678", "Algorithms", "Carol Brown", 2023)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# List books
library.list_books()

# Borrow and return books
print(f"\n{library.borrow_book('Python Programming')}")
print(f"{library.borrow_book('Python Programming')}")  # Try to borrow again
print(f"{library.return_book('Python Programming')}")

# Example 2: Shape hierarchy
class Shape:
    """Base Shape class"""
    
    def __init__(self, name):
        """Initialize shape"""
        self.name = name
    
    def area(self):
        """Calculate area (to be overridden)"""
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        """Calculate perimeter (to be overridden)"""
        raise NotImplementedError("Subclass must implement perimeter()")

class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        """Initialize rectangle"""
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        """Initialize circle"""
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate circle area"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle perimeter (circumference)"""
        return 2 * 3.14159 * self.radius

# Using shape hierarchy
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8)
]

print("\nShape areas and perimeters:")
for shape in shapes:
    print(f"{shape.name}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

print("\n" + "=" * 60)
print("END OF OBJECT-ORIENTED PROGRAMMING TUTORIAL")
print("=" * 60)

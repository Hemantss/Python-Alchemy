"""
Python Alchemy

Module:
chapters.chapter_10_python_object_model.mini_project

Design a Book and Library system that brings together the core principles of Object-Oriented Programming in Python.
"""


from dataclasses import dataclass

# -----------------------------
# Book Base Class (using @dataclass)
# -----------------------------
@dataclass
class Book:
    title: str
    author: str
    _price: float # private attribute by convention


    # Encapsulation with @property
    @property
    def price(self):
        """Get the price of the book"""
        return self._price
    

    @price.setter
    def price(self, value):
        """Set the price with validation"""
        if not Book.is_valid_price(value):
            raise ValueError("Invalid price. Must be non-negative number.")
        self._price = value

    
    # Static method for validation (utility)
    @staticmethod
    def is_valid_price(value):
        return isinstance(value, (int, float)) and value >= 0
    

    # Class method for alternative constructor
    @classmethod
    def from_string(cls, book_str):
        """Create a Book from ‘title;author;price’ string"""
        title, author, price = book_str.split(";")
        return cls(title.strip(), author.strip(), float(price.strip()))
    

# -----------------------------
# Inheritance: EBook subclass
# -----------------------------
@dataclass
class EBook(Book):
    file_size: float # in MB
    format: str = "PDF"

    def __repr__(self):
        return f"EBook(title={self.title}, author={self.author}, price={self.price}, size={self.file_size}MB, format={self.format})"
    


# -----------------------------
# Library Class
# -----------------------------
class Library:
    total_books = 0 # class-level attribute

    def __init__(self, name):
        self.name = name
        self._collection = [] # private collection of books


    # Encapsulation with @property
    @property
    def collection(self):
        """Return all books in the library"""
        return self._collection
    

    # Add a book (normal method)
    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Only Book or EBook instances can be added.")
        self._collection.append(book)
        Library.total_books += 1


    # Class method to get total number of books across all libraries
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    

    # Static method for simple search utility
    @staticmethod
    def search_by_author(books, author_name):
        """Return all books by a given author"""
        return [book for book in books if book.author.lower() == author_name.lower()]
    

    def __repr__(self):
        return f"Library(name={self.name}, total_books={len(self._collection)})"
    


# -----------------------------
# Demonstration of System
# -----------------------------
if __name__ == "__main__":
    # Create books using normal constructor
    b1 = Book("1984", "George Orwell", 20.0)
    b2 = Book("Animal Farm", "George Orwell", 15.0)
    
    # Create book using classmethod
    b3 = Book.from_string("Brave New World; Aldous Huxley; 18.5")
    
    # Create EBook (inheritance)
    eb1 = EBook("Python Alchemy", "Hemant Singh Sikarwar", 10.0, 5.2, "EPUB")
    
    # Create library and add books
    lib = Library("Central Library")
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(eb1)

    # Show library and collection
    print(lib)
    print(lib.collection)


    # Test property (price validation)
    try:
        b1.price = -5 # Will raise ValueError
    except ValueError as e:
        print("Error:", e)
    
    # Search by author using static method
    orwell_books = Library.search_by_author(lib.collection, "George Orwell")
    print("Books by George Orwell:", orwell_books)
    
    # Show total books (class-level tracking)
    print("Total books across all libraries:", Library.get_total_books())
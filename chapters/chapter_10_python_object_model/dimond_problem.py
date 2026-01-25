"""
Python Alchemy
Module:
chapters.chapter_10_python_object_model.dimond_problem

Diamond Problem Example: Hybrid Inheritance in Python
--------------------------------------------------------------------
This script demonstrates:
- Defining a class hierarchy that leads to the diamond problem.
- How Python's Method Resolution Order (MRO) resolves method calls in such cases.
The diamond problem occurs in multiple inheritance when two parent classes inherit from the same base class,
"""

class Book:
    """
    Base class for all book types.
    """
    def info(self):
        return "General book information."

class Textbook(Book):
    """
    A textbook is a type of book.
    """
    def info(self):
        return "Textbook information."

class Reference(Book):
    """
    A reference book is a type of book.
    """
    def info(self):
        return "Reference book information."

class DigitalTextbook(Textbook, Reference):  # Hybrid inheritance
    """
    A digital textbook is a type of textbook and reference book.
    """
    pass

dt = DigitalTextbook()
print(dt.info())  
print(DigitalTextbook.__mro__)  # To see the MRO

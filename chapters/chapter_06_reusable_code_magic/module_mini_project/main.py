"""
Python Alchemy

Module:
Chapters.chapter_06_reusable_code_magic.module_mini_project.main

This module demonstrates a simple calculator using modular programming.
"""

# Importing modules from the package
from my_calculator import add, subtract, multiply

# Using functions from different modules
print("10 + 5 =", add.add(10, 5))
print("10 - 5 =", subtract.subtract(10, 5))
print("10 * 5 =", multiply.multiply(10, 5))

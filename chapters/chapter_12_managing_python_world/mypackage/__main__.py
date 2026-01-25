"""
Python Alchemy

Module:
chapters.chapter_12_managing_python_world.mypackage.__main__

Main Module for Mypackage
--------------------------------
This module serves as the entry point for the mypackage package.
"""

from math_ops import add
from string_ops import greet

def main():
    """Main function to demonstrate package functionality."""
    print(greet("Ivaan"))
    print("5 + 3 =", add(5, 3))


if __name__ == "__main__":
    main()
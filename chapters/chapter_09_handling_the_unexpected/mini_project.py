"""
Python Alchemy

Module:
chapters.chapter_09_handling_the_unexpected.mini_project

Mini Project: Exception Handling, Assertions, and Logging
-----------------------------------------------------------
This program demonstrates practical use of:
- Exception handling with try, except, finally
- Assertions for validating assumptions
- Logging for tracking application flow and errors
"""

import pdb
import logging

# Configure logging
logging.basicConfig(
    filename=".\\logs\\debug_log.txt", # Log messages saved in a file
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_strings(strings):
    """
    Process a list of strings: convert to uppercase and get length.

    Parameters:
    strings (list): List of strings to process.

    Returns:
    list: List of tuples containing (uppercase string, length).
    """
    logging.info("Function process_strings started with input: %s", strings)
    results = []
    for s in strings:
        pdb.set_trace() # Start debugger here to inspect each iteration
        try:
            logging.info("Processing string: %s", s)
            upper_s = s.upper() # Potential bug if s is None
            length = len(upper_s)
            results.append((upper_s, length))
        except AttributeError as e:
            logging.error("Invalid value encountered: %s", s)
            results.append(("ERROR", 0))
    return results


# Example input (with an intentional bug: None value)
data = ["apple", "banana", None, "cherry"]
output = process_strings(data)
print("Final Results:", output)
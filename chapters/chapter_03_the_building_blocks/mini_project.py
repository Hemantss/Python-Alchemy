"""
Python Alchemy

Module:
chapters.chapter_03_the_building_blocks.mini_project
"""


# Different data types
student_name = "Ivaan" # String: represents text
age = 20 # Integer: whole number
height = 5.6 # Float: decimal number
is_enrolled = True # Boolean: True/False value
courses = ["Math", "Physics"] # List: ordered collection
grades = {"Math": 85, "Physics": 92} # Dictionary: key-value pairs

unique_ids = {101, 102, 103} # Set: unique unordered values
nothing = None # NoneType: represents "no value"

# Arithmetic operators
average = (grades["Math"] + grades["Physics"]) / 2
# ‘+’ adds values, ‘/’ divides them → calculates average grade.

# Assignment operators
age += 1 # Same as age = age + 1 → student just had a birthday.

# Comparison operators
passed = average >= 50
# ‘>=’ checks if average is at least 50 (True/False result).

# Logical operators + short-circuit evaluation
can_graduate = passed and is_enrolled
# ‘and’ only evaluates right side if left side is True → efficient check.

# Identity operators
print(student_name is "Ivaan") # True (may use string interning).
print(student_name is not "Bob") # True → identity check.

# Membership operators
print("Math" in courses) # True → "Math" is inside list.
print("Biology" not in courses) # True → "Biology" not found.

# Bitwise operators (student ID check)
id_check = 101 & 1
# Bitwise AND → checks if number is odd (1) or even (0).

# Operator precedence and parentheses
final_score = (average + age) * 2 if can_graduate else average
# Parentheses ensure ‘+’ happens before ‘*’.
# Ternary expression (x if cond else y) decides based on condition.

# Output with f-strings
print(f"Student: {student_name}, Age: {age}")
print(f"Height: {height}ft, Enrolled: {is_enrolled}")
print(f"Courses: {courses}, Grades: {grades}")
print(f"Unique IDs: {unique_ids}")
print(f"Average Grade: {average}, Passed: {passed}")
print(f"Can Graduate: {can_graduate}")
print(f"ID Bitwise Check: {id_check}")
print(f"Final Score (after precedence rules): {final_score}")
print(f"Nothing Type: {nothing}")
"""
Puthon Alchemy

Module:
chapters.chapter_07_speaking_python_language.mini_project

Mini Project: Text Data Processing with String Operations, f-Strings, and Regex
--------------------------------------------------------------------------
This program demonstrates practical use of:
- String operations: splitting, trimming
- f-Strings for dynamic and formatted output
- Regular expressions (regex) for pattern matching and data extraction
"""

import re

# Sample textual data
text = """
Users: Ivaan, Laisha, Eve, David
Emails: ivaan@example.com, laisha@test.org, eve@abc.net
Phone numbers: 123-456-7890, 9876543210
"""

# 1. String operations: splitting and trimming
users_line = text.split("\n")[1].strip()  # Extract the users line
users = users_line.replace("Users: ", "").split(", ")
print("Users list:", users)
for idx, user in enumerate(users, start=1):
    print(f"User {idx}: {user.upper()}")  # Dynamic, formatted output

# 2. Regex: extracting all emails
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
all_emails = re.findall(email_pattern, text)
print(f"Total emails found: {len(all_emails)}")
for email in all_emails:
    print(f"- {email}")

# 3. Regex: extracting phone numbers and formatting output
phone_pattern = r"\d{3}-?\d{3}-?\d{4}"
phone_numbers = re.findall(phone_pattern, text)
formatted_numbers = [f"({num[:3]}) {num[4:7]}-{num[-4:]}" for num in phone_numbers]
print("Formatted phone numbers:")
for num in formatted_numbers:
    print(num)

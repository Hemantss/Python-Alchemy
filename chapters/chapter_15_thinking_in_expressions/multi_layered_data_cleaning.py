"""
Python Alchemy

Module:
chapters.chapter_15_thinking_in_expressions.multi_layered_data_cleaning

Multi-Layered Data Cleaning Pipeline
--------------------------------
This module demonstrates a multi-layered data cleaning pipeline using
functional programming constructs like zip, filter, map, enumerate, and reduce.
"""


from functools import reduce
from datetime import datetime

# Raw data composed of partially valid and inconsistent inputs
names = ["  Ivaan", "laisha ", None, "   cHaRlie  ", "DAVID", "eve "]
emails = ["ivaan@example.com", "laisha@", "charlie@example.com", None, "david@example.com", "eve@example.com"]
signup_dates = ["2024-01-01", "invalid", "2023-11-12", "2024-03-05", "2024-02-28", "2024-01-18"]

# ---------------- Step 1: Combine datasets using zip() ----------------
records = list(zip(names, emails, signup_dates))

# ---------------- Step 2: Filter invalid entries ----------------
# Valid record must have non-null name, valid email, and valid date format.
def is_valid(record):
    name, email, date = record
    if not (name and email and "@" in email and "." in email):
        return False
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except Exception:
        return False

cleaned = list(filter(is_valid, records))

# ---------------- Step 3: Normalize using map() ----------------
def normalize(record):
    name, email, date = record
    return {
        "name": name.strip().title(),
        "email": email.lower(),
        "signup": datetime.strptime(date, "%Y-%m-%d")
    }

normalized = list(map(normalize, cleaned))

# ---------------- Step 4: Enrich data using enumerate() ----------------
# Add a unique user_id based on position
enriched = [
    {**record, "user_id": idx + 1}
    for idx, record in enumerate(normalized)
]

# ---------------- Step 5: Aggregate summary statistics with reduce() ----------------
# Example: find earliest and latest signup dates
date_range = reduce(
    lambda acc, rec: (
        min(acc[0], rec["signup"]),
        max(acc[1], rec["signup"])
    ),
    enriched,
    (enriched[0]["signup"], enriched[0]["signup"])
)

# ---------------- Display Results ----------------
print("Cleaned & Enriched Records:")
for r in enriched:
    print(r)

print("\nSignup Date Range:", date_range)
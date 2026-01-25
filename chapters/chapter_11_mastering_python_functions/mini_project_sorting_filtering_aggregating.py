"""
Python Alchemy

Module:
chapters.chapter_11_mastering_python_functions.mini_project_sorting_filtering_aggregating

Mini Project: Sorting, Filtering, and Aggregating Data with Functional Programming
-----------------------------------------------------------
This program demonstrates practical use of:
- Sorting data using custom keys
- Filtering data with lambda functions
- Aggregating data using reduce
"""


# Example dataset: a list of product records
products = [
    { "name": "Laptop",
    "category": "Electronics",
    "price": 1200,
    "rating": 4.5},
    { "name": "Coffee Maker",
    "category": "Home",
    "price": 150,
    "rating": 4.2},
    { "name": "Headphones",
    "category": "Electronics",
    "price": 200,
    "rating": 4.8},
    { "name": "Blender",
    "category": "Home",
    "price": 90,
    "rating": 4.0},
    { "name": "Smartwatch",
    "category": "Electronics",
    "price": 300,
    "rating": 4.6},
]

# 1. Filter products by category
electronics = list(filter(lambda p: p["category"] == "Electronics", products))

# 2. Sort by rating (highest first)
sorted_products = sorted(electronics, key=lambda p: p["rating"], reverse=True)

# 3. Aggregate: calculate average price of filtered items
from functools import reduce
avg_price = reduce(lambda acc, p: acc + p["price"], sorted_products, 0) / len(sorted_products)

# Display results
print("Top-rated Electronics:")
for item in sorted_products:
    print(f"- {item['name']} (Rating: {item['rating']}, Price: ${item['price']})")
print(f"\nAverage Price: ${avg_price:.2f}")
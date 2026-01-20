# Function Patterns
# 🔹 Pattern 1 — Validator Functions
# Check something and return True / False
#
# Structure
# def is_valid(value):
#     return condition
#
# Validator functions return booleans and contain no side effects
#
# 🔹 Pattern 2 — Transformer Functions
# Purpose
# Take data → change it → return new data
#
# Structure
# def transform(data):
#     result = []
#     for item in data:
#         result.append(modified_item)
#     return result
#
# 🔹 Pattern 3 — Filter Functions
# Purpose
# Remove unwanted data
#
# Example
# def filter_positive(numbers):
#     result = []
#     for n in numbers:
#         if n > 0:
#             result.append(n)
#     return result

# This is data preprocessing.
#
# 🔹 Pattern 4 — Controller Functions
# Purpose
#
# Coordinate logic (call other functions)
#
# Example
# def process_numbers(numbers):
#     clean = filter_positive(numbers)
#     return square_numbers(clean)

# 💬 Interview phrase: “Controller functions orchestrate smaller functions.”
#
# 🔹 Pattern 5 — Action Functions
# Purpose
# Do something (print, save, send)
#
# def show_message(msg):
#     print(msg)
#
# No return needed
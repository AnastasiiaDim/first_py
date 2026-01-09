# 🔴 Function Composition
#
# A function is_valid_number(n)
# → returns True if n is between 1 and 100
# A function filter_valid_numbers(numbers)
# → uses the first function
# → returns only valid numbers

def is_valid_number(n):
    return n > 0 and n <= 100 # 0 < n <= 100

def filter_valid_numbers(numbers):
    valid_numbers = []
    for n in numbers:
        if is_valid_number(n):
            valid_numbers.append(n)
    return valid_numbers
# 🟡 Safe Data Filter (Lists + Functions)
# ❓ Task
# Write a function that:
# Receives a list of numbers
# Returns a new list with:
# Only numbers greater than 0
# Ignore zeros and negatives

def positive_numbers(numbers):
    result = []

    for number in numbers:
        if number > 0:
            result.append(number)

    return result

# 🔥 Bonus — Data Filter Function
# Function receives a list
# Returns a new list with only positive numbers

def filter_positive_numbers(numbers):
    result = []

    for number in numbers:
        if number > 0:
            result.append(number)

    return result

# data = [-2, -15, 2, 15, 0, 84, -100]
# clean_data = filter_positive_numbers(data)
# print(clean_data)
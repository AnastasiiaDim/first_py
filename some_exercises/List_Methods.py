# .append() - add an element

# .pop() - removes and returns an element

# numbers = [10, 20, 30]
# last = numbers.pop()
# print(last)
# print(numbers)
#
# Output - 30 [10, 20]

# .pop()  by index - removes first element

# .remove() - removes the first occurrence of a value; searches by value, not index

# in - checks if a value exists in a list

# .count() - counts how many times a value appears
# ________________________________________________

# 🟢 Task 1 — Shopping Cart

# cart = []
#
# cart.append("apple")
# cart.append("orange")
# cart.append("banana")
#
# cart.remove("banana")
#
# print(cart)

# 🟡 Task 2 — Access Control

# allowed_users = ['admin', 'Ana', 'guest']
#
# name = input("What is your name? : ")
#
# if name in allowed_users:
#     print("Access granted")
# else:
#     print("Access denied")

# 🔴 Task 3 — Duplicate Counter
#
# numbers = [14, 5, 27, 5, 42, 14, 9, 5, 63, 27]
#
# duplicates = []
#
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)
#
# print(duplicates)
#
# 🔥 Bonus — Safe Removal
#
# tasks = ["delete", "continue", "update"]
#
# target = "copy"
#
# if target in tasks:
#     tasks.remove(target)
#     print(f"Task {target} deleted.")
#
# else:
#     print(f"Task {target} does not exist.")


# 🟢 Task 1 — Data Filter
# You are given a list of numbers.
# Print only the valid readings.
# Rules:
# Skip negative numbers
# Skip numbers greater than 100
# Print the rest

# for i in range(1, 105):
#     if i <= 0:
#         continue
#     elif i > 100:
#         break
#     print(i)

# 🟡 Task 2 — Login Attempts Simulation
# Task:
#
# Allow 3 attempts
# Password = "ai2025"
# If input is empty → skip attempt
# If correct → stop immediately
# After each wrong attempt → print attempts left
# If all attempts are used → lock account

# password = "ai2025"
# attempts = 0
#
# while attempts < 3:
#     guess = input("Enter your password: ")
#     if guess == password:
#         print("Access granted!")
#         break
#     elif guess == "":
#         continue
#     else:
#         attempts += 1
#     if guess != password:
#         print("Wrong password!")
#
# if attempts == 3:
#     print("You have used all attempts!")

# 🟡 Task 3 — Duplicate Detector (Nested Loops)
# Given a list of numbers, print only the duplicates.
# numbers = [1, 2, 3, 2, 4, 5, 1]
#
# for i in range (len(numbers)):
#     for j in range (i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(numbers[i])

# 🔴 Task 4 — Pair Generator
# Given two lists:
#
# X = [1, 2, 3]
# Y = ['a', 'b']
# Print all possible pairs

# x = [1, 2, 3]
# y = ['a', 'b']
#
# for i in range (len(x)):
#     for j in range (len(y)):
#         print(f"({x[i]}, {y[j]})")

# 🔴 Task 5 — Pattern Recognition
# Print this pattern:
#
# 1 1 1 1
# 2 2 2
# 3 3
# 4

# for i in range(1, 5):
#     for j in range(5 - i):
#         print(i, end='')
#     print()

# 🔥 Bonus Task — Early Exit Optimization
# Given a 2D list:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Find the number 5 and:
# Print "Found"
# Stop all loops immediately

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# found = False
#
# for i in matrix:
#     for j in i:
#         if j == 5:
#             found = True
#             print("Found")
#             break
#     if found:
#         break

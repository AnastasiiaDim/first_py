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
numbers = [1, 2, 3, 2, 4, 5, 1]

for i in range (len(numbers)):
    for j in range (i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])


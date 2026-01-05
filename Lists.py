# 🟢 Task 1.1 — List Reader
#
# numbers = [1, 2, 3, 4, 5]
#
# # Loop directly over values (cleaner when index is not needed)
# for num in numbers:
#     print(num)
#
# # Print total number of elements
# print("Total numbers:", len(numbers))


# 🟢 Task 1.2 — Index Practice
#
# first_names = ["Alex", "Susan", "John", "Michael", "Ana"]
# last_names = ["Doe", "Dill", "Buff", "Truck", "Donal"]
# # ___________
# # for first, last in zip(first_names, last_names):
# #     print(first, last)
# # ___________
# first_names[2] = "Python"
#
# for i in range(0, len(first_names)):
#     print(first_names[i], last_names[i])

# 🟡 Task 2.1 — Data Cleaner
#
# data = [10, -5, 25, 200, 0, 50]
# clean_data = []
#
# for n in data:
#     if n < 0:
#         continue
#     if n > 100:
#         continue
#
#     clean_data.append(n)
#
# print("Clean data:", clean_data)

# 🟡 Task 2.2 — Counter Program
#
# numbers = [-42, 7, 0, -15, 88, -3, 21, -11, 54, 1]
#
# positive = 0
# negative = 0
# zero = 0
#
# for number in numbers:
#     if number < 0:
#         negative += 1
#     elif number > 0:
#         positive += 1
#     elif number == 0:
#         zero += 1
#
# print("Positive numbers: ", positive)
# print("Negative numbers: ", negative)
# print("Zero: ", zero)

# 🔴 Task 3.1 — Largest Value Finder

# numbers = [-42, 7, 0, -15, 88, -3, 21, -11, 54, 1]
#
# largest = numbers[0]
#
# for num in mumbers:
#     if num > largest:
#         largest = num
#
# print("Largest number: ", largest)

# 🔴 Task 3.2 — Duplicate Finder
#
# numbers = [14, 5, 27, 5, 42, 14, 9, 5, 63, 27]
#
# duplicates = []
# seen = []
#
# for num in numbers:
#     if num in seen and num not in duplicates:
#         duplicates.append(num)
#     else:
#         seen.append(num)
#
# print("Duplicates: ", duplicates)

# 🔥 Task 4.1 — Dataset Validator

# dataset = [25, -1, 30, None, 150, 45]
#
# valid_data = []
# skipped = 0
#
# for item in dataset:
#     if item is None:
#         skipped += 1
#         continue
#     elif item < 0 or item > 100:
#         skipped += 1
#         continue
#     valid_data.append(item)
#
# print("Number of skipped: ", skipped)
# print("Valid Data: ", valid_data)

# 🔥 Task 4.2 — Sliding Window Simulation
# My first try -->

# numbers = [1, 2, 3, 4, 5]
#
# number = 0
#
# list_1 = [0] * 3 #[0, 0, 0]
# list_2 = [0] * 3
# list_3 = [0] * 3
#
# for i in range(3):
#     if i == 0:
#         list_1[0] = 0
#         list_2[0] = 1
#         list_3[0] = 2
#     elif i == 1:
#         list_1[i] = 1
#         list_2[i] = 2
#         list_3[i] = 3
#     elif i == 2:
#         list_1[i] = \
#             2
#         list_2[i] = 3
#         list_3[i] = 4
#
# # for number in range(len(numbers)):
# #     list_1.extend([number + 1, number + 2, number + 3])
# #     list_2.extend([number + 2, number + 3, number + 4])
# #     list_3.extend([number + 3, number + 4, number + 5])
# #     break
#
# print(list_1, ',', list_2, ',', list_3)

# My second try with corrected logic -->

# numbers = [1, 2, 3, 4, 5]
#
# window_size = 3
#
# for i in range(len(numbers) - window_size + 1):
#     window = numbers



# Nested loops like a clock:
# Outer loop = hours
# Inner loop = minutes
# For each hour, all minutes pass.
# 👉 The inner loop runs completely for each iteration of the outer loop.
# Syntax
# for i in range(3):
#     for j in range(4):
#         print(i, j)

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
#
# symbol = input("Enter the symbol: ")
#
# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()

# NESTED LOOPS

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == j:
#             print("X", end="")
#         else:
#             print("O", end="")
#     print()

# 🟢 Task 1 — Rectangle of Stars
# rows = 3
# column = 5
# symbol = "*"
#
# for x in range(rows):
#     for y in range(column):
#         print(symbol, end="")
#     print()

# 🟡 Task 2 — Multiplication Table

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end=" ")
#     print()

# 🔴 Task 3 — Number Pattern
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
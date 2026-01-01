# WHILE Loop — Repeat while a condition is True

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# FOR Loop — Repeat for Each Item
# for item in sequence:
#     code_to_repeat

# TASK 1
#
# password = ""
#
# while password != "python":
#     password = input("Enter your password: ")
# print("Access granted")
#
# TASK 2
#
# number = int(input("Enter a number: "))
#
# for number in range(1, number + 1):
#     print(number)
#
# # TASK 3
# password = ""
# attempts = 0
#
# while  attempts <3:
#     password = input("Enter your password: ")
#     attempts += 1
#     if password == "admin":
#         print("Login successful")
#         break
#     else:
#         print("Wrong password. Try again!")
#
# if password != "admin":
#     print("You have used all attempts. Account locked!")
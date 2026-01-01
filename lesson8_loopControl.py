# TASK 1 -- Skip Odd Numbers
# for i in range(1,21):
#     if i % 2 != 0:
#         continue
#     print(i)
#
# TASK 2 -- Input Cleaner
# attempts = 5
#
# for i in range(attempts):
#     number = int(input("Enter a number: "))
#     if number < 0:
#         continue
#
#     print(number)

#
# TASK 3 -- Password Validator
# password_correct = "python"
# attempts = 0
#
# while attempts < 3:
#     guess = input("Enter your password: ")
#     if guess == password_correct:
#         print("Access granted")
#         break
#     elif guess == "":
#         print("Empty password, try again")
#         continue
#     else:
#         attempts += 1
#     if attempts < 3:
#         print("Incorrect password. Attempts left: ", 3 - attempts)
#
# if attempts == 3:
#     print("Access denied")

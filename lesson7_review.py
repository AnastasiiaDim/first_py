# TASK 1
# number = int(input("Enter a number: "))
#
# while number < 0:
#     number = int(input("Enter a number: "))
#
# print("Thank you")

# TASK 2
# n = int(input("Please enter a number: "))
#
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)

# TASK 3
password_correct = "python"
attempts = 0
# 1. Loop while attempts are less than 3
while attempts < 3:
    guess = input("Enter your password: ")
    if guess == password_correct:
        print("Login Successful")
        break # Stop immediately because they got it right
    else:
        attempts += 1 # Add 1 to the count of failed tries
        # 2. Only print 'Incorrect' if they still have tries left or just failed
    if attempts < 3:
        print("Incorrect password. Attempts left: ", 3 - attempts)
# 3. Use logic outside the loop to check if they failed all 3 times
if attempts == 3:
    print("Account locked!")



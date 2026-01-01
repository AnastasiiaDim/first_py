# AND — BOTH conditions must be True

# OR — AT LEAST ONE condition must be True

# NOT — Reverses the condition

# Task 1
# age = int(input("Please enter your age: "))
# user_answer = input("Do you have an ID? (yes/no): ").lower()
# has_id = (user_answer == "yes")
#
# if age >= 18 and has_id == True:
#     print("Access granted")
# else:
#     print("Access denied")

# Task 2
admin = input("Are you an administrator? (yes/no): ").lower()
is_admin = admin == "yes"
ticket = input("Do you have a ticket (yes/no): ").lower()
is_ticket = ticket == "yes"

if is_admin or is_ticket:
    print("Access granted")
else:
    print("Access denied")

# Task 3
# user_answer = input("Is your account blocked (yes/no): ").lower()
# is_blocked = user_answer == "yes"
#
# if not is_blocked:
#     print("Welcome")
# else:
#     print("Account blocked")
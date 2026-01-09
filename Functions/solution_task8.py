# 🟡 Password Validator (Logic Fix)
# Write a function that:
# Receives a password
# Returns True if:
# Password is "python"
# Password is NOT empty
# Otherwise returns False

def correct_password(password):
    if password != "" and password == "python":
        return True
    else:
        return False

# user_input = input("Enter your password: ")
# if correct_password(user_input):
#     print("Password Correct")
# else:
#     print("Password Incorrect")
users = {
    "Ana" : "user",
    "Tom" : "student",
    "Alex" : "viewer"
}

passwords = {
    "Ana" : "python",
    "Tom" : "java",
    "Alex" : "css"
}

def login(username, password_provided):
    if username not in users:
        return "User not found"

    if passwords.get(username) == password_provided:
        return "Success"
    else:
        return "Incorrect Password"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    result = login(user_input, password_input)

    if result == "Success":
        print(f"Welcome, {user_input}!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Error: {result}. You have {remaining} attempts left.\n")
        else:
            print("Sorry, you have no more attempts.\n")











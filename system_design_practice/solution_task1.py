#Secure Login System

users = {
    "ana" : {"age": 21, "role": "user"},
    "admin" : {"age": 30, "role": "admin"}
}

roles = {
    "admin" : {"read", "write", "delete", "add_user"},
    "user" : {"read"}
}

passwords = {
    "ana" : "python",
    "admin" : "system"
}

def user_exists(username):
    return username in users

def password_valid(username, password):
    return passwords.get(username) == password

def has_permission(role, action):
    allowed_actions = roles.get(role, set())
    return action in allowed_actions

def main_controller():
    while True:
        who_is = input("Enter username: ")
        if user_exists(who_is):
            break
        else:
            print("User not found")

    attempts = 0
    max_attempts = 3
    login_success = False

    while attempts < max_attempts:
        password_input = input("Enter password: ")
        if password_valid(who_is, password_input):
            login_success = True
            break

        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password! You have {remaining} attempts left.")
        else:
            print("Access blocked: Too many attempts!")

    if login_success:
        print(f"Welcome {who_is}!")
        user_role = users[who_is]["role"]

        while True:
            action  = input(f"What do you want to do? (or type 'exit' to exit): ").lower()
            if action == "exit":
                print("Logging out...")
                break

            if has_permission(user_role, action):
                print("Success! Action Allowed!")

            else:
                print("Access denied: You don't have permission to do that.")

main_controller()




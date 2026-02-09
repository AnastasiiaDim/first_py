users = {
    "ana" : {"age": 21, "role": "user"},
    "admin" : {"age": 30, "role": "admin"}
}

roles = {
    "admin" : {"read", "write", "delete", "add_user"},
    "user" : {"read"}
}

def is_admin(username):
    if username in users:
        return users[username]["role"] == "admin"
    return False

def username_available(new_username):
    return new_username not in users

def add_user_logic(admin_name, new_name, age, new_role):
    if not is_admin(admin_name):
        return "Denied: Only admins can add users"
    if not username_available(new_name):
        return "Error: username is already taken"

    if age < 18:
        return "Error: User must be 18 or older"

    if new_role not in roles:
        return "Error: Role does not exist"

    users[new_name] = {"age": age, "role": new_role}

    return "Successfully added user!"

def registration_controller():
    who_are_you = input("Enter your name: ")
    if not is_admin(who_are_you):
        print("Denied: Only admins can register users")
        return

    while True:
        newname = input("\nEnter user's name (or type 'exit'): ")
        if newname.lower() == "exit":
            break

        newage = input("Enter user's age: ")

        if newage.isdigit():
            newage = int(newage)
        else:
            print("Error: Age must be a digit")
            continue

        new_role = input("Enter user's role: ")

        result = add_user_logic(who_are_you, newname, newage, new_role)
        print(result)

        print("Current users:", users)






users = {
    "ana" : {"age": 21, "role": "user"},
    "admin" : {"age": 30, "role": "admin"}
}

roles = {
    "admin" : {"read", "write", "delete", "add_user"},
    "user" : {"read"}
}

def user_exists(username):
    return username in users

def has_permission(role, action):
    allowed_actions = roles.get(role, set())
    return action in allowed_actions

def add_user(new_username, new_age, new_role):
    users[new_username] = {"age" : int(new_age), "role" : new_role}
    if new_role not in roles:
        return "Invalid role"
    if new_username in users:
        return "User already exists"
    return f"User {new_username} successfully added."

def main_controller():
    who_is = input("Enter username: ")

    if not user_exists(who_is):
        print("Access Denied")
        return

    current_user_role = users[who_is]["role"]

    target_action = input("Enter action (e.g., read): ")
    if not has_permission(current_user_role, target_action):
        print("Access Denied")
        return

    print("Allowed!")

    if target_action == "add_user":
        while True:
            name = input("Enter new username: ")
            age = input("Enter new age: ")

            if age.isdigit():
                age = int(age)
            else:
                print("Error. Age must be a digit!")
                continue

            role = input("Enter new role: ")

            result = add_user(name, age, role)
            print(result)

            print("Updated database:", users)

            break

main_controller()


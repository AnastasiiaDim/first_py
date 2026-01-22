users = {
    "ana": "student",
    "admin": "admin",
    "user": "user"
}

def check_user(user):
    return users.get(user, "User not found")


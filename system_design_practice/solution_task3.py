# Config Management System

CONFIG = (
    ("Title", "My Awesome App"),
    ("Version", 3.14),
    ("Debug", True),
    ("Max_Users", 100)
)

def get_config_value(target_key):
    for name, value in CONFIG:
        if name == target_key:
            return value
    return None

def print_config():
    print("--- Current Configuration ---")
    for name, value in CONFIG:
        print(f"Setting: {name} | Value: {value}")
    print("-----------------------------")


# USERS_DATA = (
#     ("admin", "London", "Active"),
#     ("ana", "Paris", "Away"),
#     ("ivan", "Moscow", "Banned")
# )
#
# def get_user_status(username):
#     for name, city, status in USERS_DATA:
#         if username == name:
#             return status
#     return None

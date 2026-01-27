# Using a list of user dictionary
users = [
    {"name": "Ana", "age": 21},
    {"name": "Tom", "age": 17},
    {"name": "Alex"}
]
# Using list

def get_valid_users(data):
    valid_users = []
    for user in data:
        age = user.get("age")

        if age is not None and age > 18:
            valid_users.append(user)

    return valid_users

result = get_valid_users(users)
print(result)

# Using dictionary
# def clean_data(data):
#     valid_users = {}
#
#     for key, info in data.items():
#         age = info.get("age")
#         if age is not None and age >= 18:
#             valid_users[key] = info
#
#     return valid_users
#
# print(clean_data(users))

# dict[key] = value --> картотека[номер_папки] = папка

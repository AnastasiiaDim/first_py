class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def is_admin(self):
        return self.role == "admin"

user1 = User("ana", "admin")
user2 = User("python", "user")

print(user1.is_admin())
print(user2.is_admin())
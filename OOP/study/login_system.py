class User:
    def __init__(self, username, age, role, password):
        self.username = username
        self.age = age
        self.role = role
        self.password = password

class AuthSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def login(self, username, password):
        if username not in self.users:
            return False
        return self.users[username].password == password

system = AuthSystem()
system.add_user(User("ana", 21, "user", "python"))
system.add_user(User("admin", 30, "admin", "system"))

print(system.login("ana", "python"))
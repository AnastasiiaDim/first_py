roles = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}

role = input("Enter role name: ")

if role in roles:
    print("Your permissions ->", roles[role])
else:
    print("Role not found")

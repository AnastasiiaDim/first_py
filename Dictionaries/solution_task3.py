users = {
    "ana": {"age": 21, "role": "student"},
    "admin": {"age": 30, "role": "admin"}
}
for name, info in users.items():
    role = info["role"]
    print(f"{name} -> {role}")
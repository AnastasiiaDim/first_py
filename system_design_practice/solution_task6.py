# Permission-Based Feature Toggle
users = {
    "ana": {"role": "user"},
    "admin_boss": {"role": "admin"}
}

features = {
    "export": {"admin"},
    "delete": {"admin"},
    "view": {"admin", "user"},
    "profile": {"admin", "user"}
}

def feature_enabled(username, feature_name):
    if username not in users:
        return False
    user_role = users[username]["role"]

    if feature_name not in features:
        return False

    return user_role in features[feature_name]


print(feature_enabled("admin_boss", "export"))
print(feature_enabled("ana", "delete"))

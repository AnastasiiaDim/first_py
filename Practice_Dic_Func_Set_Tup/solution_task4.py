permissions = {
    "admin" : {"edit", "delete", "add", "update", "view"},
    "user" : {"view", "update", "delete"},
    "visitor" : {"view"}
}

def permit_validator(role, action):
    allowed_actions = permissions.get(role, set())
    return action in allowed_actions



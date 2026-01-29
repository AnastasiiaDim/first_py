admin = {"read", "write", "delete", "copy"}
user = {"read", "copy"}

def get_shared_permissions(role1, role2):
    # The '&' operator finds what is common between both sets
    shared = role1 & role2
    return shared

print(get_shared_permissions(admin, user))



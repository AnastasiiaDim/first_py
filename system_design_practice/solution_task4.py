# Audit Log System

track = [
    {"user": "admin", "action": "add_user"},
    {"user": "ana", "action": "read"}
]

def log_action(username, action):
    new_entry = {"user": username, "action": action}
    track.append(new_entry)
    return "Action added."

def get_logs_by_user(username):
    print(f"--- Logs for user: {username} ---")
    found = False

    for entry in track:
        if entry["user"] == username:
            print(f"Action: {entry['action']}")
            found = True

    if not found:
        print("No logs found for this user")
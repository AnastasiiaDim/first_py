active_users = ["Weeknd", "Drake", "Kendrick", "KennyW", "Taylor"]
banned_users = ["Drake", "Trump", "Taylor"]
active = set(active_users)
banned = set(banned_users)

active -= banned #allowed_users = active - banned

print(active)

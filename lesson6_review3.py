account_active = input("Is you account active? (yes/no): ").lower()
account_blocked = input("Is you account blocked? (yes/no): ").lower()

if account_active == "yes" and not account_blocked == "yes":
    print("Account access granted")
else:
    print("Account access denied")
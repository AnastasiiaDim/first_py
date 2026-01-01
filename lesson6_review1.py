username = input("Enter your username: ").lower()
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
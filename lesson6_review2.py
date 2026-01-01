age = int(input("Enter your age: "))
permission = input("Do you have parental permission? (yes/no): ").lower()

if age >= 18 or (permission == "yes" and age <18):
    print("Access allowed")
else:
    print("Access denied")
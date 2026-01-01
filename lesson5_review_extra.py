birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year

if age < 13:
    print("You are a child")
elif age <= 17:
    print("You are a teenager")
elif age <= 65:
    print("You are an adult")
else:
    print("You are a senior")
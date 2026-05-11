birth_year = int(input("Enter your birth year: "))
current_year = 2025
user_chosen = int(input("Enter a year to see your future age: "))

age = current_year - birth_year
age_in_future = user_chosen - birth_year

print("Your age is ", age)
print("You will be ", age_in_future, "years old")

print("Welcome to Basic Calculator! Let's start!🧮")

while True:
    print("\nSelect an option:")
    print("1. Add ➕")
    print("2. Subtract ➖")
    print("3. Multiply ✖️")
    print("4. Divide ➗")
    print("5. Exit 🏃‍")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Bye-bye!")
        break

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == '1':
        print("Result: ", num1 + num2)
    elif choice == '2':
        print("Result: ", num1 - num2)
    elif choice == '3':
        print("Result: ", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("❗️ Error! You cannot divide by zero!")
        else:
            print("Result: ", num1 / num2)
    else:
        print("❗️ Invalid input. Please enter a number from 1 to 5.")

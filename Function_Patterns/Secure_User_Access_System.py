# 🎯 Project Goal
# You are building a login system that:
# checks usernames
# checks passwords
# limits attempts
# uses functions correctly
# follows clean function patterns

users = ["admin", "user1", "ana", "boss"]

def username_validator(username, users_list):
    if username in users_list:
        return True
    else:
        return False

    #return username in users_list

def password_validator(password):

    if password == "python":
        return True
    else:
        return False

def controller():

    while True:
        guess = input("Please enter your username: ").lower()

        if username_validator(guess, users):
            print("User found. Let's go next!")
            attempts = 0

            while attempts < 3:

                guess_password = input("Please enter your password: ")
                if password_validator(guess_password):
                    print("Logged in. Welcome!")
                    return
                else:
                    attempts += 1

                if attempts < 3:
                    print("Incorrect data. Attempts left: ", 3 - attempts)

            if attempts == 3:
                print("You have used all attempts. Access denied.")
                return

        else:
            print("Invalid username. Try again.")

controller()
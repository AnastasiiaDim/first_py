# 🟢 Exercise 1 — Fix the Function (Naming & Logic)
# Fix it so that:
# The function returns True if a user exists
# Returns False otherwise
# Uses correct naming
# Does NOT modify the input list

def check_user(user_list, name):

    if name in user_list:
        return True
    else:
        return False

# OR
#
# def check_user(user_list, name):
#     return name in user_list
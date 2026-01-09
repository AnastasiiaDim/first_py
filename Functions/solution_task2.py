# 🟡 Task 2 — Age Checker
# Function receives age
# Returns "Adult" or "Minor"

def age_check(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = age_check(21)
print(result)
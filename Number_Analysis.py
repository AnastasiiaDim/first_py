# TASK 4
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "Even")
    elif i % 3 == 0:
        print(i, "Odd and divisible by 3")
    else:
        print(i, "Odd")
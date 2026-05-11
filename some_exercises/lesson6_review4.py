task_priority = input("What is task priority? (high/medium/low): ").lower()
urgency = input("Is it urgent? (yes/no): ").lower()

if task_priority == "high" or urgency == "yes":
    print("Execute immediately")
else:
    print("Schedule for later")
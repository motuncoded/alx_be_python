task = str(input("Enter your daily task: "))
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is this time-bound? (yes/no): ").lower()


match (priority, time_bound):
    case ("high", "yes"):
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Note: {task} is a high priority task. Make sure to complete it soon.")
    case ("medium", "yes"):
        print(f"Reminder: {task} is a medium priority task with a deadline.")
    case ("medium", "no"):
        print(f"Note: {task} is a medium priority task. You can do it later.")
    case ("low", "yes"):
        print(f"Reminder: {task} is a low priority task with a deadline.")
    case ("low", "no"):
        print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
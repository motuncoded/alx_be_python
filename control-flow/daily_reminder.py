task = str(input("Enter your task: "))
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()


# /tmp/correction/8827246924403990929007500907962317739109_5/100740/34965/control-flow/daily_reminder.py doesn't contain match\s+priority\s*: / /tmp/correction/8827246924403990929007500907962317739109_5/100740/34965/control-flow/daily_reminder.py doesn't contain high['\"]\s*:

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "high":
        print(f"Note: '{task}' is a high priority task. Make sure to complete it soon.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task with a deadline.")
    case "medium":
        print(f"Note: '{task}' is a medium priority task. You can do it later.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task with a deadline.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
tasks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        print("\nYour tasks:")

        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

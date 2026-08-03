print("===== Student Task Manager =====")

name = input("Enter your name: ")

print("\nHello", name)

tasks = []

while True:
    print("\n===== MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Thank you for using Student Task Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
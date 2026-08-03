print("===== Student Task Manager =====")

name = input("Enter your name: ")

print("\nHello", name)

tasks = []

while True:
    print("\n===== MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task_name = input("Enter a task: ")

        task = {
            "name": task_name,
            "completed": False
        }

        tasks.append(task)

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):

                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i}. {task['name']} - [{status}]")

    # Mark Task as Completed
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            task_number = int(input("Enter the task number to complete: "))

            if 1 <= task_number <= len(tasks):

                tasks[task_number - 1]["completed"] = True

                print("Task marked as completed!")

            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Thank you for using Student Task Manager!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")
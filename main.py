import json
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
print("===== Student Task Manager =====")

name = input("Enter your name: ")

print("\nHello", name)

tasks = load_tasks()

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task_name = input("Enter a task: ")

        task = {
            "name": task_name,
            "completed": False
        }

        tasks.append(task)
        save_tasks(tasks)
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
                save_tasks(tasks)
                print("Task marked as completed successfully!")

            else:
                print("Invalid task number.")

    # Exit
    # Delete Task
    elif choice == "4":

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

        task_number = int(input("Enter the task number to delete: "))

        if 1 <= task_number <= len(tasks):

            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['name']}' deleted successfully!")

        else:
            print("Invalid task number.")

# Exit
    elif choice == "5":
            print("Thank you for using Student Task Manager!")
            break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")
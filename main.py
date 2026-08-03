print("Welcome to Student Task Manager!")

name = input("Enter your name: ")

print("\nHello", name)
print("Welcome to your task manager!")

tasks = []

task = input("\nEnter a task: ")

tasks.append(task)

print("\nTask added successfully!")

print("\nYour Tasks:")

for task in tasks:
    print("-", task)
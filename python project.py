#!/usr/bin/python3import time
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in your To-Do list.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

def mark_task_completed(tasks):
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

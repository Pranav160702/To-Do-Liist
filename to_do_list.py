import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task['done'] else "Pending"
        print(f"{i}. {task['description']} [{status}]")

def add_task():
    description = input("Enter the task description: ")
    tasks = load_tasks()
    tasks.append({'description': description, 'done': False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def mark_task_done():
    list_tasks()
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        tasks = load_tasks()
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            save_tasks(tasks)
            print(f"Marked task {index + 1} as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Error: Task number must be an integer.")

def delete_task():
    list_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        tasks = load_tasks()
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Error: Task number must be an integer.")

def show_menu():
    print("""
    To-Do List Menu
    1. List all tasks
    2. Add a new task
    3. Mark a task as done
    4. Delete a task
    5. Exit
    """)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

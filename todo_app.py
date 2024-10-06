tasks = []

def add_task():
    """Function to add a new task"""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    """Function to view all tasks"""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

def delete_task():
    """Function to delete a task"""
    view_tasks() 
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    """Main menu for the to-do list app"""
    while True:
        print("\nTo-Do List Application")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()

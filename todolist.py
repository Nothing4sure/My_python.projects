# Initialize an empty list to store tasks
tasks = []

def show_tasks():
    """Function to display all the tasks."""
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{index}. {task['task']} - {task['priority']} - {status}")
    else:
        print("\nYour to-do list is empty.")

def add_task():
    """Function to add a task to the list."""
    task = input("Enter the task you want to add: ")
    priority = input("Enter priority (High, Medium, Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority! Setting to Medium.")
        priority = "Medium"
    
    tasks.append({"task": task, "priority": priority, "completed": False})
    print(f"Task '{task}' with priority '{priority}' added to your to-do list.")

def delete_task():
    """Function to delete a task from the list."""
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    """Function to mark a task as completed."""
    show_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list app."""
    while True:
        print("\nTo-Do List Application")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

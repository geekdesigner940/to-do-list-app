import os

def display_tasks(tasks):
    """
    Display the current list of tasks.

    Parameters:
    - tasks (list of dict): The list of tasks, each represented as a dictionary.

    Returns:
    - None
    """
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['name']}")

def add_task(tasks, name):
    """
    Add a new task to the list.

    Parameters:
    - tasks (list of dict): The list of tasks, each represented as a dictionary.
    - name (str): The name of the task to be added.

    Returns:
    - None
    """
    tasks.append({"name": name, "completed": False})
    print(f"Task '{name}' added successfully!")

def save_tasks_to_file(tasks, filename):
    """
    Save the tasks to a file with a custom name.

    Parameters:
    - tasks (list of dict): The list of tasks, each represented as a dictionary.
    - filename (str): The name of the file to save tasks to.

    Returns:
    - None
    """
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task["name"] + "\n")
    print(f"Tasks saved to '{filename}' successfully!")

def load_tasks_from_file(filename):
    """
    Load tasks from a file.

    Parameters:
    - filename (str): The name of the file to load tasks from.

    Returns:
    - list: The list of tasks loaded from the file.
    """
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task_name = line.strip()
                tasks.append({"name": task_name, "completed": False})
    return tasks

def main():
    tasks = []

    # Custom directory path to store files
    custom_directory = input("Enter the custom directory path to store files (leave empty for the current directory): ")
    if custom_directory:
        os.makedirs(custom_directory, exist_ok=True)
        os.chdir(custom_directory)

    # Custom filename to save tasks
    custom_filename = input("Enter the custom filename to save tasks (leave empty for default 'tasks.txt'): ")
    if not custom_filename:
        custom_filename = "tasks.txt"

    # Load tasks from the file if it exists
    tasks = load_tasks_from_file(custom_filename)

    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks to File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task_name = input("Enter the task name: ")
            add_task(tasks, task_name)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task['name']}' removed successfully!")
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")
        elif choice == "4":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                tasks[task_index]["completed"] = True
                print("Task marked as complete!")
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")
        elif choice == "5":
            save_tasks_to_file(tasks, custom_filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

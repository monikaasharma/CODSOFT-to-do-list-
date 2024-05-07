# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)

# Function to remove a task from the to-do list
def remove_task(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
    else:
        print("Task not found in the to-do list.")

# Function to display the current to-do list
def display_list(todo_list):
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

# Main function
def main():
    todo_list = []  # Initialize an empty list for the to-do tasks
    while True:
        print("\nSelect an option:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display the to-do list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(todo_list, task)
        elif choice == '3':
            display_list(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

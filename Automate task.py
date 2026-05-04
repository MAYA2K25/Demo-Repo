tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i, task)

def delete_task(task_number):
    if task_number > 0 and task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")


while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
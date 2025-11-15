#
to_do = []
def show_tasks():
    if not to_do:
        print("No tasks exist")
    else:
        for i, task in enumerate(to_do,1): 
            print(f"{i} {task} ")

def add_task(task):
    to_do.append(task)
    print(f"{task} is added to your Task list")

def delete(index):
    if 0 < index <= len(to_do):
        removed = to_do.pop(index-1)
        print(f"{removed} task is removed")
    else:
        print("This task not exist")

while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        index = int(input("Enter task number to delete: "))
        delete(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")






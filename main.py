import sys
from app_logic import add_task, list_tasks, delete_task, mark_done

def print_tasks():
    tasks = list_tasks()
    if not tasks:
        print("No tasks yet!")
        return

    for i, task in enumerate(tasks):
        status = "[✔]" if task['done'] else "[ ]"
        print(f"{i + 1}. {status} {task['description']}")

def show_menu():
    print("\nTo-Do App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            print_tasks()

        elif choice == '2':
            desc = input("Enter task description: ").strip()
            if desc:
                add_task(desc)
                print("Task added.")

        elif choice == '3':
            print_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
                print("Task deleted.")
            except:
                print("Invalid input.")

        elif choice == '4':
            print_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index)
                print("Task marked as done.")
            except:
                print("Invalid input.")

        elif choice == '5':
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

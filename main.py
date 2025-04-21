import os
import datetime
import time
from playsound import playsound

TODO_FILE = "todo.txt"
DONE_FILE = "done.txt"


def add(task):
    # Check if task is already in the todo file
    tasks = read_file(TODO_FILE)
    if task in tasks:
        tasks.remove(task)  # Refresh it by moving it to the end

    tasks.append(task)
    write_file(TODO_FILE, tasks)
    print(f'Added todo: "{task}"')


def delete(task_number):
    tasks = read_file(TODO_FILE)
    if task_number < 1 or task_number > len(tasks):
        print(f"ERROR...! Task #{task_number} does not exist! No task is deleted!")
        return

    tasks.pop(task_number - 1)
    write_file(TODO_FILE, tasks)
    print(f"Deleted todo #{task_number}")


def done(task_number):
    tasks = read_file(TODO_FILE)
    if task_number < 1 or task_number > len(tasks):
        print(f"ERROR...! Task #{task_number} doesn't exist!")
        return

    completed_task = tasks.pop(task_number - 1)
    write_file(TODO_FILE, tasks)

    # Add to done file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(DONE_FILE, "a") as done_file:
        done_file.write(f"x {timestamp} {completed_task}\n")
    print(f"Marked todo #{task_number} as done.")


def list_tasks():
    tasks = read_file(TODO_FILE)
    if not tasks:
        print("There are no pending todos.")
    else:
        for i, task in enumerate(reversed(tasks), start=1):
            print(f"[{len(tasks) - i + 1}] {task}")


def help():
    print("How to use this TODO APP :-")
    print("$ python todo_app.py add \"todo item\"        # Add a new todo item")
    print("$ python todo_app.py del NUMBER             # Delete a todo item")
    print("$ python todo_app.py done NUMBER            # Complete a todo item")
    print("$ python todo_app.py ls                     # Show remaining todo items")
    print("$ python todo_app.py help                   # Show How to use")
    print("$ python todo_app.py report                 # Display Statistics of the app.")
    print("$ python todo_app.py remind TIME \"todo item\" # Set a reminder with sound")


def report():
    pending = len(read_file(TODO_FILE))
    completed = len(read_file(DONE_FILE))
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"{date} Pending Tasks: {pending} Completed Tasks: {completed}")


def remind(time_str, task):
    try:
        remind_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= remind_time:
                add(task)
                print(f"Reminder: {task}")
                playsound("reminder_sound.mp3")  # Replace with your sound file
                break
            time.sleep(30)
    except ValueError:
        print("Invalid time format! Use HH:MM (24-hour format).")


def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def write_file(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def main():
    import sys
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <command>")
        help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("ERROR...! Missing todo string! Nothing added!")
        else:
            add(sys.argv[2])
    elif command == "del":
        if len(sys.argv) < 3:
            print("ERROR...! Missing task number! No task is deleted!")
        else:
            delete(int(sys.argv[2]))
    elif command == "done":
        if len(sys.argv) < 3:
            print("ERROR...! Missing task number! No task is marked completed!")
        else:
            done(int(sys.argv[2]))
    elif command == "ls":
        list_tasks()
    elif command == "help":
        help()
    elif command == "report":
        report()
    elif command == "remind":
        if len(sys.argv) < 4:
            print("ERROR...! Missing time or task for reminder!")
        else:
            remind(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command. Use 'python todo_app.py help' for usage instructions.")


if __name__ == "__main__":
    main()
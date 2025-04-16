import json
import os
import threading
from datetime import datetime
from time import sleep
from playsound import playsound

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, reminder_time=None):
    tasks = load_tasks()
    tasks.append({
        'description': description,
        'done': False,
        'reminder_time': reminder_time
    })
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)

def reminder_watcher():
    while True:
        tasks = load_tasks()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        for task in tasks:
            if not task.get('done') and task.get('reminder_time') == now:
                print(f"\n🔔 Reminder: {task['description']}")
                playsound('reminder_sound.mp3')
                task['done'] = True
                save_tasks(tasks)
        sleep(30)  # check every 30 seconds

def start_reminder_thread():
    import threading
    t = threading.Thread(target=reminder_watcher, daemon=True)
    t.start()


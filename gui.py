import tkinter as tk
from tkinter import messagebox, simpledialog
from app_logic import add_task, load_tasks, delete_task, mark_done, start_reminder_thread

start_reminder_thread()

def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    tasks = load_tasks()
    for i, task in enumerate(tasks):
        frame = tk.Frame(task_frame, bg="#f0f0f0", pady=5)
        frame.pack(fill="x")

        status = "✔" if task['done'] else "❌"
        label = tk.Label(frame, text=f"{status} {task['description']}", anchor="w", bg="#f0f0f0")
        label.pack(side="left", expand=True)

        if not task['done']:
            done_btn = tk.Button(frame, text="Done", command=lambda i=i: [mark_done(i), refresh_tasks()])
            done_btn.pack(side="right", padx=5)

        del_btn = tk.Button(frame, text="Delete", command=lambda i=i: [delete_task(i), refresh_tasks()])
        del_btn.pack(side="right", padx=5)

desc = simpledialog.askstring("New Task", "Enter task description:")


import tkinter as tk
from tkinter import messagebox, simpledialog 
import os
import json
from datetime import datetime


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Initialize tasks
        self.tasks = []

        # Load tasks from file
        self.load_tasks()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Task List

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=80)
        self.task_listbox.pack(pady=10)
      
        # Add Task Button
        add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.pack()

        # Remove Task Button
        remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_task_button.pack()

        # Mark as Completed Button
        mark_completed_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        mark_completed_button.pack()

        # Refresh List Button
        refresh_button = tk.Button(self.root, text="Refresh List", command=self.refresh_list)
        refresh_button.pack()

        # Exit Button
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack()

        # Populate initial list
        self.refresh_list()

    def new_method(self):
        print

    def add_task(self):
        task_text = simpledialog.askstring("Add Task", "Enter task:")
        if task_text:
            priority = simpledialog.askstring("Task Priority", "Enter priority (High/Medium/Low):")
            due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")

            new_task = {
                "task": task_text,
                "priority": priority,
                "due_date": due_date,
                "completed": False
            }

            self.tasks.append(new_task)
            self.save_tasks()
            self.refresh_list()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askyesno("Confirm", "Are you sure you want to remove this task?")
            if confirmed:
                del self.tasks[selected_index[0]]
                self.save_tasks()
                self.refresh_list()

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["completed"] = True
            self.save_tasks()
            self.refresh_list()

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else " Not completed"
            self.task_listbox.insert(tk.END, f"{task['task']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

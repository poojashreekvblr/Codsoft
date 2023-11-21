import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=0, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "Your to-do list is empty.")
        else:
            task_list = "\n".join(task["task"] for task in self.tasks)
            messagebox.showinfo("To-Do List", f"Your to-do list:\n{task_list}")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.task_listbox.itemconfig(index, {'bg': 'light gray'})
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

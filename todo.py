import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = ToDoList()

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.tasks_listbox.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.pack()

        self.save_button = tk.Button(self.root, text="Save and Quit", command=self.save_and_quit)
        self.save_button.pack()

        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_task_list()

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.delete_task(index)
            self.update_task_list()

    def mark_as_completed(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.mark_as_completed(index)
            self.update_task_list()

    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task_info in self.todo_list.tasks:
            status = " [X]" if task_info["completed"] else " [ ]"
            self.tasks_listbox.insert(tk.END, f"{task_info['task']}{status}")

    def save_and_quit(self):
        self.todo_list.save_to_file("todo.txt")
        messagebox.showinfo("Info", "To-Do List saved. Quitting...")
        self.root.quit()

    def load_tasks(self):
        self.todo_list.load_from_file("todo.txt")
        self.update_task_list()

class ToDoList:
    # Your ToDoList class definition remains unchanged.

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

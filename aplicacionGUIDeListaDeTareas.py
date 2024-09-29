import tkinter as tk
from tkinter import ttk

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tareas")
        self.master.geometry("400x300")

        self.task_input = tk.Entry(self.master, width=30)
        self.task_input.grid(row=0, column=0, padx=5, pady=5)
        self.task_input.bind("<Return>", self.add_task)

        self.add_button = tk.Button(self.master, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_list = ttk.Treeview(self.master, columns=("Task", "Status"), show="headings")
        self.task_list.heading("Task", text="Tarea")
        self.task_list.heading("Status", text="Estado")
        self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.complete_button = tk.Button(self.master, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.task_list.bind("<Double-1>", self.on_double_click)

    def add_task(self, event=None):
        task = self.task_input.get()
        if task:
            self.task_list.insert("", tk.END, values=(task, "Pendiente"))
            self.task_input.delete(0, tk.END)

    def mark_completed(self):
        selected_item = self.task_list.selection()
        if selected_item:
            self.task_list.item(selected_item, values=(self.task_list.item(selected_item)['values'][0], "Completada"))

    def delete_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            self.task_list.delete(selected_item)

    def on_double_click(self, event):
        item = self.task_list.selection()
        if item:
            self.mark_completed()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
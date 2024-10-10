import tkinter as tk
from tkinter import ttk

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tareas")
        self.master.geometry("400x300")

        self.tasks = []

        # Campo de entrada
        self.task_entry = ttk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        self.task_entry.bind("<Return>", self.add_task)

        # Botón Añadir
        self.add_button = ttk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Lista de tareas
        self.task_list = tk.Listbox(master, width=50, height=10)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Botón Completar
        self.complete_button = ttk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        # Botón Eliminar
        self.delete_button = ttk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        # Atajos de teclado
        self.master.bind("<c>", self.complete_task)
        self.master.bind("<Delete>", self.delete_task)
        self.master.bind("<Escape>", self.close_app)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def complete_task(self, event=None):
        try:
            index = self.task_list.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_task_list()
        except IndexError:
            pass

    def delete_task(self, event=None):
        try:
            index = self.task_list.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            pass

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "✓ " if task["completed"] else "  "
            self.task_list.insert(tk.END, f"{status}{task['task']}")
            if task["completed"]:
                self.task_list.itemconfig(tk.END, {'fg': 'gray'})

    def close_app(self, event=None):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

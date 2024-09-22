import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import datetime

# Función para agregar un evento a la lista
def agregar_evento():
    fecha = cal.get_date()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")

# Eliminar un evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Seleccionar evento", "Por favor, seleccione un evento para eliminar.")

# Salir de la aplicación
def salir():
    ventana.quit()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Frame para la selección de fecha y entrada de datos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=20)

# Calendario para seleccionar la fecha
label_fecha = tk.Label(frame_entrada, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=10)
cal = Calendar(frame_entrada, selectmode="day", date_pattern="yyyy-mm-dd")
cal.grid(row=0, column=1, padx=10)

# Campo de entrada para la hora
label_hora = tk.Label(frame_entrada, text="Hora:")
label_hora.grid(row=1, column=0, padx=10)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=10)

# Campo de entrada para la descripción del evento
label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=10)
entrada_descripcion = tk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1, padx=10)

# Botón para agregar un evento
boton_agregar = tk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=3, columnspan=2, pady=10)

# Frame para la lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=20)

# TreeView para mostrar los eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Eliminar un evento seleccionado
boton_eliminar = tk.Button(ventana, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(pady=10)

# Salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

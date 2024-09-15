import tkinter as tk
from tkinter import ttk

class AplicacionGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("GUI Básica")
        self.ventana.geometry("400x300")

        # Etiqueta y campo de texto
        self.etiqueta = tk.Label(ventana, text="Agrege informacion:")
        self.etiqueta.pack(pady=5)
        self.campo_texto = tk.Entry(ventana, width=30)
        self.campo_texto.pack(pady=5)

        # Botones
        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar_elemento)
        self.boton_agregar.pack(pady=5)
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_seleccion)
        self.boton_limpiar.pack(pady=5)

        # Tabla
        self.tabla = ttk.Treeview(ventana, columns=("Elemento",), show="headings")
        self.tabla.heading("Elemento", text="Elementos agragdos")
        self.tabla.pack(pady=10, fill=tk.BOTH, expand=True)

    def agregar_elemento(self):
        elemento = self.campo_texto.get()
        if elemento:
            self.tabla.insert("", tk.END, values=(elemento,))
            self.campo_texto.delete(0, tk.END)

    def limpiar_seleccion(self):
        seleccion = self.tabla.selection()
        for item in seleccion:
            self.tabla.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
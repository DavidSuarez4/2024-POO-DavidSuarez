import json

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    # Métodos para obtener y establecer atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
            print("Producto añadido.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.get_nombre().lower() == nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            productos_dict = {id: vars(producto) for id, producto in self.productos.items()}
            json.dump(productos_dict, f)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_dict = json.load(f)
                self.productos = {id: Producto(**datos) for id, datos in productos_dict.items()}
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error al leer el archivo.")

# Interfaz de Usuario
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (presione Enter para omitir): ")
            precio = input("Ingrese nuevo precio (presione Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "6":
            archivo = input("Ingrese nombre del archivo para guardar el inventario: ")
            inventario.guardar_en_archivo(archivo)
        elif opcion == "7":
            archivo = input("Ingrese nombre del archivo para cargar el inventario: ")
            inventario.cargar_desde_archivo(archivo)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

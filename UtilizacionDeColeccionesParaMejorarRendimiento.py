class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return self.libros_prestados


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro_a_devolver = None
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    libro_a_devolver = libro
                    break
            if libro_a_devolver:
                usuario.devolver_libro(libro_a_devolver)
                self.libros[isbn] = libro_a_devolver

    def buscar_libro(self, **kwargs):
        resultado = []
        for libro in self.libros.values():
            coincidir = True
            for clave, valor in kwargs.items():
                if getattr(libro, clave) != valor:
                    coincidir = False
                    break
            if coincidir:
                resultado.append(libro)
        return resultado

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].listar_libros_prestados()


# Ejemplo de Uso
if __name__ == "__main__":
    # Crear una instancia de la biblioteca
    biblioteca = Biblioteca()

    # Crear y añadir libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
    libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", "67890")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar un usuario
    usuario1 = Usuario("Juan Pérez", "001")
    biblioteca.registrar_usuario(usuario1)

    # Prestar un libro
    biblioteca.prestar_libro("001", "12345")

    # Listar libros prestados
    print(usuario1.listar_libros_prestados())

    # Devolver un libro
    biblioteca.devolver_libro("001", "12345")

    # Buscar libros por autor
    resultados = biblioteca.buscar_libro(autor="Gabriel García Márquez")
    print(resultados)

class Mascota:

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota..
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        print(f"¡Nueva mascota! {self.nombre} ({self.especie}, {self.edad} años)")

    def __del__(self):
        """
        Destructor de la clase Mascota.
        """
        print(f"¡Hasta luego! {self.nombre}")

    def comer(self):
        """
        Método que simula que la mascota come.
        """
        print(f"{self.nombre} ({self.especie}) está comiendo")

    def dormir(self):
        """
        Método que simula que la mascota duerme.
        """
        print(f"{self.nombre} ({self.especie}) está durmiendo")


# Ejemplo de uso
perro1 = Mascota("Boris", "perro", 2)
perro1.comer()
perro1.dormir()

gato1 = Mascota("Blanca", "gato", 1)
gato1.comer()
gato1.dormir()
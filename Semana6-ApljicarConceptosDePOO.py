# Definición de la clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar_idioma(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases derivadas")

# Clase derivada de Persona
class Español(Persona):
    def __init__(self, nombre, edad, nacionalidad):
        super().__init__(nombre, edad)
        self.__nacionalidad = nacionalidad  # Atributo encapsulado

    # Método para obtener el valor del atributo encapsulado
    def obtener_nacionalidad(self):
        return self.__nacionalidad

    # Método para cambiar el valor del atributo encapsulado
    def cambiar_nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

    # Sobrescribir el método hablar_idioma, demostrando polimorfismo
    def hablar_idioma(self):
        return "Yo hablo español"

# Otra clase derivada de Persona
class Ingles(Persona):
    def __init__(self, nombre, edad, pais):
        super().__init__(nombre, edad)
        self.pais = pais

    # Sobrescribir el método hablar_idioma, demostrando polimorfismo
    def hablar_idioma(self):
        return "I speak English"


# Creación de instancias de las clases y demostración de funcionalidad

# Instancia de la clase Español
persona_espanola = Español("David", 19, "Ecuador")
print(f"Nombre: {persona_espanola.nombre}, Edad: {persona_espanola.edad}, Nacionalidad: {persona_espanola.obtener_nacionalidad()}")
print(f"Idioma: {persona_espanola.hablar_idioma()}")

# Cambiando el valor del atributo encapsulado
persona_espanola.cambiar_nacionalidad("México")
print(f"Nueva Nacionalidad: {persona_espanola.obtener_nacionalidad()}")

# Instancia de la clase Ingles
persona_inglesa = Ingles("Will", 25, "Estados Unidos")
print(f"Nombre: {persona_inglesa.nombre}, Edad: {persona_inglesa.edad}, País: {persona_inglesa.pais}")
print(f"Idioma: {persona_inglesa.hablar_idioma()}")

# Plimorfismo
personas = [persona_espanola, persona_inglesa]
for persona in personas:
    print(f"{persona.nombre} dice: {persona.hablar_idioma()}")

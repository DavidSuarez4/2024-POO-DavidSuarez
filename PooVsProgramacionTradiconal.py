            #Programacion tradicional
def ingresar_datos_diarios():
  temperaturas = []
  for i in range(7):
    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temperaturas.append(temperatura)
  return temperaturas
#Funcion para calcular el pronedio semanal
def calcular_promedio_semanal(temperaturas):
  promedio = sum(temperaturas) / len(temperaturas)
  return promedio

temperaturas_semanales = ingresar_datos_diarios()
promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
print(f"Usando programacion tradicional el resultado es: {promedio_semanal:.2f}")



           #Programacion Orientada a Objetos
#Crear la clase
class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []
    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    clima_semanal = ClimaSemanal()
    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        clima_semanal.ingresar_temperatura(temp)
    promedio = clima_semanal.calcular_promedio()
    print(f"El resultado usando POO es: {promedio:.2f}")

if __name__ == "__main__":
    main()





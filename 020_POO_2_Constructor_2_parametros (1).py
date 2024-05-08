# 🙄

# POO

# CREACIÓN DE UNA CLASE


class Coche:

    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):  # Método constructor. double underscore = dunder
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha

    # Declaración de métodos
    def arrancar(self):  # self hace referencia a la instancia de clase.
        self.is_enMarcha = True  # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"

        # Declaración de una instancia de clase, objeto de clase o ejemplar de clase.


miCoche = Coche(250, 120, 4, 900, "rojo", False)

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
miCoche.ruedas = 7
print("El largo del coche es de", miCoche.largo, "cm.")
miCoche.arrancar()
print(miCoche.estado())

# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arrancado:", miCoche.arrancar())

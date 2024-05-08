# 🙄


# POO

# CREACIÓN DE UNA CLASE


class Coche():
# Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False

# Declaración de métodos
    def arrancar(self):             # self hace referencia a la instancia de clase.
        self.is_enMarcha = True     # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"    

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = Coche()

miCoche.__ruedas = 9
print("Mi coche tiene",miCoche.__ruedas, "ruedas.")
help(Coche)
# Crea una jerarquía de clases para un sistema de trabajo en una empresa. Comienza con una clase base Persona (abuelo), luego crea una clase derivada Empleado (padre) que herede de persona, y finalmente, una clase Gerente (hijo) que herede de Empleado.
# Además, añade una clase Habilidad que represente las habilidades adicionales que un empleado puede tener. 
# Haz que Generente herede tanto de Empleado como de Habilidad (herencia multiple).

# Asegurate de:

# Utilizar atributos y métodos en cada clase.
# Sobreesribir métodos en las clases derivadas.
# Utilizar super() para llamar a métodos de las clases base.
# Mostrar el uso de la herencia múltiple.

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def presentarse(self):
    print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

class Empleado(Persona):
   def __init__(self, nombre, edad, profesion):
     super().__init__(nombre, edad)
     self.profesion = profesion  
     
   def presentarse(self):
     print(f"Hola soy {self.nombre}, tengo {self.edad} años, y soy {self.profesion}")

class Habilidad:
   def __init__(self, habilidad):
     self.habilidad = habilidad
  

class Gerente(Empleado, Habilidad):
  def __init__(self, nombre, edad, profesion, habilidad, empresa):
    Empleado.__init__(self, nombre, edad, profesion)
    Habilidad.__init__(self, habilidad)
    self.empresa = empresa 
    
  def presentarse(self):
    print(f"Hola soy {self.nombre}, tengo {self.edad}, soy {self.profesion}, tengo esta habilidad: {self.habilidad}, y trabajo en la empresa: {self.empresa}")
    
    
hombre = Persona("Luis", 23)
hombre.presentarse()


luis = Empleado("Luis", 23, "mecanico")
luis.presentarse()

juan = Gerente("Juan", 55, "Gerente", "mandar", "Corte ingles")
juan.presentarse()
from math import pi

"""
def area(r):
  areaC = pi*(r**2)
  return areaC
"""

# Versión con la excepción de ValueError

"""
def area(r):
  # Verificamos si el valor es negativo
  if r < 0:
    raise ValueError("No se permiten valores negativos")
    # print("No negativos")
  
  areaC = pi*(r**2)
  return areaC
"""

# Versión con la excepción de TypeError

def area(r):
  
  # Verificamos por los tipos correctos
  if type(r) not in [float, int]:
    raise TypeError("Sólo se pueden usar flotantes y enteros")
  
  # Verificamos si el valor es negativo
  if r < 0:
    raise ValueError("No se permiten valores negativos")
    # print("No negativos")
  
  areaC = pi*(r**2)
  return areaC



# valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

# for v in valores:
#   areaCalculada = area(v)
#   print('Para el valor', v, 'el área es', areaCalculada)



# Tenemos que poner en consola para ejecutarlo:
#   python -m unittest test_testing01.py

# Nota: Podemos ejecutar automáticamente las
# pruebas usando el comando:
#   python -m unittest discover
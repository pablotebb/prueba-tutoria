# Para ejecutarlo ponemos en la consola
#   python -m unittest test_testing01.py
# Importamos unittest
import unittest
# Importamos el método a usar
from testing01 import area 
from math import pi 

# Creamos una clase que desciende de TestCase
class TestArea(unittest.TestCase):
  
  # Definimos el método donde se lleva a cabo el test 
  # debe iniciar con test
  def test_area(self):
    
    # Hacemos un test para un valor que sabemos cual es el resultado
    
    print("-----Test valores de resultado conocido-----")
    self.assertAlmostEqual(area(1), pi)
    self.assertAlmostEqual(area(0), 0)
    # self.assertAlmostEqual(area(0), 1) # Incorrecto
    self.assertAlmostEqual(area(3), pi*(3**2))
    
  ###################################################################  
    
  # Ahora verificamos si la función regresa el tipo correcto
  # de excepción dependiendo del valor
  # Experimentamos con radios de valor negativo
  
  def test_negativos(self):
    print("-----Test de valores negativos-----")
    
    # Indicamos el tipo de excepción, la función y el valor que sabemos
    # debe generar la excepción
    self.assertRaises(ValueError, area, -1)
    
    # Vemos que nos indica que no se levanta la excepción
    # esto nos debe de llevar a modificar el código para colocar 
    # la excepción
    
  ################################################################### 
    
  # Verificamos que recibiremos el tipo correcto de datos
  
  def test_tipos(self):
    
    # El tipo de excepción debe ser TypeError
    # Hacemos una prueba para cada tipo que sabemos que no es 
    # compatible con el parámetro
    
    print("-----Test de tipos no compatibles-----")
    
    self.assertRaises(TypeError, area, True)
    self.assertRaises(TypeError, area, 'hola')
    self.assertRaises(TypeError, area, 2+3j)
    
    # Vemos que nos indica que no se levanta la excepción
    # esto nos debe de llevar a modificar el código para colocar
    # la excepción
    
  
  


# Nota - 
# Mirar Youtube, bien explicado:
#   17) https://www.youtube.com/watch?v=pc-M9vCvmQ0&t=562s
#   18) https://www.youtube.com/watch?v=Kiz_5d9-WQY
#   19) https://www.youtube.com/watch?v=AK4SsGEw6Lk&t=98s
  
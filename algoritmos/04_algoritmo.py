def codigo_4(array):
  for k in range(len(array)):
    if( array[k] % 2 == 0 ):
      return k
    
  return null



l_dame_primer_par = [1, 3, 5, 6, 7, 8, 9, 2]
print(codigo_4(l_dame_primer_par)) # 3

# El siguiente código tiene como fin encontrar el primer
# número par de una lista de números

# Algunos algoritmos pueden tener distintos tiempos
# de ejecución, teniendo el mismo tamaño de los datos
# y los mismos recursos computacionales. Esto es
# debido a que, dependiendo de los datos, a veces se
# llegue a una solución en la primera iteración, o bien
# tener que recorrer todos los datos.

# En "EL PEOR CASO" ni siquiera tenga un número par, porque
# recorrería todas las instrucciones

# Para "EL MEJOR CASO" tendríamos una complejidad
# algorítmica:
#       F(x)=1
# Para "EL PEOR DE LOS CASOS" la complejidad algorítmica
# sería:
#       F(x)=n

# Para expresar "EL PEOR CASO" usaremos una notación
# conocida como “O Grande” y se escribe:
#       O(n)

# Para medir un algoritmo necesitamos recurrir al escenario de 
# "PEOR CASO" y con un gran volumen de datos



# Crear una tupla con elementos duplicados
tupla = (1, 2, 3, 4, 5, 5, 6, 7, 7, 8)

# Acceder a uno de los elementos de la tupla
elemento = tupla[3]  # Accediendo al cuarto elemento (índice 3)

# Mostrar el elemento obtenido
print("Elemento accedido:", elemento) # Elemento accedido: 4

print("Accediendo al elemento 5 directamente: ", tupla[5]) # 5

# Visualizar todos los elementos de la tupla
print("Todos los elementos de la tupla:")
for elemento in tupla:
    print(elemento)
# 1
# 2
# 3
# 4
# 5
# 5
# 6
# 7
# 7
# 8

tupla[3] = 10  # Da error, es inmutable
# Traceback (most recent call last):
#   File "C:\Users\pablo\Downloads\Curso ibm python\Master\04 PYTHON\Estructuras de datos\02_tupla.py", line 26, in <module>
#     tupla[3] = 10
# TypeError: 'tuple' object does not support item assignment



# Tupla (tuple); es una colección ordenada e
# inmutable. Permite miembros duplicados.

# No permiten añadir, eliminar, mover elementos
# (no append, extend, remove)
# (son inmutables)
# Pero si puedes eliminar la tupla completa
#  Ej del tupla


# Pueden utilizarse como claves en un diccionario
# (las listas no).

# Las tuplas se pueden usar sin paréntesis, una cadena es por 
# tanto una tupla, y es inmutable
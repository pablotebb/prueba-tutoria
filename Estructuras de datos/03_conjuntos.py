
# Crear un conjunto con elementos duplicados
conjunto = {1, 2, 3, 4, 5, 5, 6, 7, 7, 8}

# Acceder a un elemento del conjunto
elemento = next(iter(conjunto))  # Accediendo al primer elemento (no hay un orden definido en los conjuntos)

# Mostrar el elemento obtenido
print("Elemento accedido:", elemento) # Elemento accedido: 1

# Mostrar todos los elementos del conjunto
print("Todos los elementos del conjunto:")
for elemento in conjunto:
    print(elemento)
# Todos los elementos del conjunto:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8




# Conjuntos (Set); es una colección que no está
# ordenada ni indexada. No hay miembros
# duplicados.

#  Los sets son conjuntos de objetos mutables
# no ordenados, (únicos y no ordenados), que se basan
# en la noción matemática de conjuntos. 

# No obstante, un conjunto no puede incluir objetos
# mutables como listas, diccionarios, e incluso otros
# conjuntos.
# Son útiles cuando queremos trabajar con datos
# masivos y queremos extraer información relevante
# de ellos
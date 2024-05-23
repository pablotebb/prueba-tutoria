
# Crear un diccionario con miembros repetidos
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5}

# Modificar un elemento del diccionario
diccionario['c'] = 10

# Mostrar un elemento específico del diccionario
print("Elemento 'c' modificado:", diccionario['c'])
# Elemento 'c' modificado: 10

# Mostrar todos los elementos del diccionario
print("Todos los elementos del diccionario:")
for clave, valor in diccionario.items():
    print(clave, ":", valor)
# Todos los elementos del diccionario:
# a : 1
# b : 2
# c : 10
# d : 4
# e : 5
# f : 5




# Diccionario (Dictionary); es una colección
# desordenada, modificable e indexada. No hay
# miembros duplicados.
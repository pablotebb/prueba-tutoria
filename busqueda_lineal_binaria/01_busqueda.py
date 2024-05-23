from array import array

def buscar(lista, nombre_buscado):
    tamano_lista = len(lista)
    for actual in range(0, tamano_lista):
      if (lista[actual] == nombre_buscado):
        return actual
    return -1

def main():
  lista_de_alumnos = sorted(importar_lista('../data/lista_alumnos'))
  posicion_del_alumno = buscar(lista_de_alumnos, "Wanessa")
  print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))
  

def importar_lista(archivo):
  lista = []
  with open(archivo) as tf:
    lines = tf.read().split('","')
  for line in lines:
    lista.append(line)
  return lista


if __name__ == "__main__":
  main()
  
# Busqueda lineal
# O(N)
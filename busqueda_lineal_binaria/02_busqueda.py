from array import array

def buscar(lista, nombre_buscado):
    tamano_lista = len(lista)
    for actual in range(0, tamano_lista):
      if (lista[actual] == nombre_buscado):
        return actual
    return -1

def main():
  lista_de_alumnos = ["Brendo",
  "Erica", "Monica", "Nico", "Paulo",
  "Rodrigo", "Wanessa"]
  
  for i in range(0, 3500):
    posicion_del_alumno = buscar(lista_de_alumnos, "Wanessa")
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

  

if __name__ == "__main__":
  main()
  
# Busqueda lineal
# O(N)
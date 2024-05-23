
def bin(a,x,low,high):
  ans = -1
  if low==high: ans = -1
  else:
    mid = (low+((high-low)//2))
    if x < a[mid]: ans = bin(a,x,low,mid)
    elif x > a[mid]: ans = bin(a,x,mid+1,high)
    else: ans = mid
  return ans

# Definir el array ordenado
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Definir el objetivo que deseas buscar
objetivo = 13

# Llamar a la función bin para buscar el objetivo en el array
resultado = bin(arr, objetivo, 0, len(arr))

# Verificar el resultado
if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {resultado}.")
    # El elemento 13 se encuentra en el índice 6.
else:
    print(f"El elemento {objetivo} no se encuentra en el array.")

# Logarítmico: O(log x)
# No suelen ser muchos. Estos algoritmos indican que
# el tiempo es menor que el tamaño de los datos de
# entrada. No importa indicar la base del logaritmo. Un
# ejemplo es una búsqueda dicotómica. 

# Este algoritmo busca un elemento en un array
# ordenado dividiendo el array en 2 mitades, identifica
# en cuál de las mitades se encuentra, luego divide esa
# parte en 2 mitades iguales y busca nuevamente hasta
# encontrar el elemento, es un algoritmo recursivo


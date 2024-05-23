def selection_sort(arr, n):
  for i in range(n):
    ## para almacenar el índice del elemento mínimo
    min_element_index = i
    for j in range(i + 1, n):
      ## comprobando y reemplazando el índice mínimo del elemento
      if arr[j] < arr[min_element_index]:
        min_element_index = j
        ## intercambiando el elemento actual con el elemento mínimo
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

if __name__ == '__main__':
  ## inicialización del array
  arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
  selection_sort(arr, 9)
  ## imprimiendo el array
  print(str(arr))

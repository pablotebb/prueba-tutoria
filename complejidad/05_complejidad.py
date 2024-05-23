
# %%time
def iterador_multiplicado(x:list) -> list:
  iterador = len(x)
  incremento = 1
  while(iterador > 0):
    iterador -= incremento
    incremento *= (incremento + 1)
    
  return x

lista = list(range(1, 1001))

print(iterador_multiplicado(lista))

# Wall time: 0 ns

# Complejidad O(log(n))
# Logarithmic Time

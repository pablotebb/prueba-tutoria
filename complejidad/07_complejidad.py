# %%time
import math

def iterador_incremento_exponencial(x:list) -> list:
  iterador = len(x)
  incremento = 1
  while(iterador > 0):
    iterador -= pow(incremento, 2)
    incremento += 1
    
  return x

lista = list(range(1, 1001))

print(iterador_incremento_exponencial(lista))

# Wall time: 0 ns

# Complejidad O(log(log(n)))
# Logarithmic from
# Logarithmic Time

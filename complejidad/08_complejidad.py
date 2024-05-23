
import numpy as np

# %%time

def calculo_bit_o_ejemplo(y:list) -> str:
  
  iterador = -len(y) # k
  incremento = 1 # k
  q_list = y # k
  
  while(iterador < 0): # log(n)
    iterador /= incremento # k
    incremento += 1 # k
    
  for p in y: # n
    for q in y: # n -> n * n
      for r in y: # n -> n * n * n
        r
    
  return "La Complejidad es n*n*n, n cubo"


y = list(np.random.randint(low=1,high=500000, size=999))

print(calculo_bit_o_ejemplo(y))

# Wall time: 14.7 s
# 'La Complejidad es n*n*n, n cubo

# Cálculo de la complejidad
# Algorítmica del Ejemplo

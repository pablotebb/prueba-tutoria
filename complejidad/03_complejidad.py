# %%time
def iterador_normal(x:list) -> list:
  contador = len(x)
  
  while(contador > 0):
    contador -= 1
    
  return x

lista = list(range(1, 1001))

print(iterador_normal(lista))

# Wall time: 5.31 


# Complejidad O(n) Linear Time

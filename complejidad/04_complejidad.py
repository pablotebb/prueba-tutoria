
# %%time
def iterador_anidado(x:list) -> list:
  
  contador_externo = len(x)//1000
  contador_interno = len(x)//1000
  
  while(contador_externo > 0):
    contador_externo -= 1
    for i in range(contador_interno):
      i
    
  return x

lista = list(range(1, 1001))


print(iterador_anidado(lista))


# Wall time: 5min 29s

# Complejidad O(n2)
# Quadratic Time

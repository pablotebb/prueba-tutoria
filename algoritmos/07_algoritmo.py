
def polinomico(number):
  x = 0
  for i in range(1,number):
    for j in range(1,number):
      x += i + j
        
  for i in range(1,number):
    for j in range(1,number):
      for k in range(1,number):
        x += i * j * k
  
  return x

print(polinomico(2)) # 3
print(polinomico(3)) # 39
print(polinomico(4)) # 252

# Polinómico: O(x^c),c > 0
# Son los algoritmos más comunes. Cuando c es 2 se
# le llama cuadrático, cuando es 3 se le llama cúbico, y
# en general, polinómico. Cuando n es muy grande
# suelen ser muy complicados. Estos algoritmos suelen
# tener bucles anidados. Si tienen 2 bucles anidados
# sería un cuadrático. 

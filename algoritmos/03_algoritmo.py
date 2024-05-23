def codigo_3(number):
  a = 0
  for j in range(1, number+1):
    for k in range(1, number+1):
      a += a + ( j*k )
      
  return a


print(codigo_3(2)) # 24

# En el código 3 tenemos un bucle anidado. Cada vez
# que ejecute un ciclo el otro se ejecuta n veces
# también. Lo cual sería n veces n. La complejidad
# quedaría:
#         F(x) = n(elevado a 2)+1
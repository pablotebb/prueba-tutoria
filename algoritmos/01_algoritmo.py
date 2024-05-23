

def codigo_1( number ):
  a = 0
  for j in range(1, number+1):
    a += a + j
    
  for k in range(number, 0, -1):
    a -= 1
    a *= 2
  return a


print(codigo_1(2)) # 10

# Es claro que el tiempo crece linealmente con respecto al valor de entrada
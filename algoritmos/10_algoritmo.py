def exponencial(n):
  if n==1 or n==2:
    return 1
  return exponencial(n-1)+exponencial(n-2)


print(exponencial(4)) # 3

# Exponencial: O(c^x).
# Es una de las peores complejidades algorítmicas.
# Sube demasiado a medida que crece los datos de
# entrada. Puede verse en la Figura como crece una
# función de este tipo. Un ejemplo de este código es la
# solución de Fibonacci, el cual genera bucles 2
# recursividades en cada ejecución.

# Ver tabla:
#   https://www.bigocheatsheet.com/
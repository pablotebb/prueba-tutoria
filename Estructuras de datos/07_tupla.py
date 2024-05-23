
x = ("apple", "banana", "cherry")

y = list(x) # convertimos a lista

y[1] = "kiwi" # modificamos

print(y) #["apple", "kiwi", "cherry"]

x = tuple(y) # convertimos de nuevo a tupla

print(x) #("apple", "kiwi", "cherry")


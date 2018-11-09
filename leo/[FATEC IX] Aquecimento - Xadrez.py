pecas = [int(x) for x in input().split(" ")]

numero_ideal_de_pecas = [1, 1, 2, 2, 2, 8]
resultado = []

for i in range(0, len(pecas)):
  resultado.append(numero_ideal_de_pecas[i] - pecas[i])
  
print(' '.join([str(x) for x in resultado]))
  
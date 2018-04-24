# Tempo: 3 min

entrada = int(input())

divisoresPossiveis = list(range(1, entrada+1))
divisores = 0

for value in divisoresPossiveis:
    if entrada % value == 0:
        divisores += 1

print(divisores)

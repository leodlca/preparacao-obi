# Tempo: 23min

dario = 0
xerxes = 0

jogadas = []
opcoes = [0, 1, 2, 3, 4, 0, 1]

limite = int(input())
count = 1

while limite >= count:
    jogada = input()
    jogada = jogada.split(" ")
    jogadas.append(jogada)
    count += 1

for jogada in jogadas:
    jogadaDario = int(jogada[0])
    jogadaXerxes = int(jogada[1])
    if jogadaDario == jogadaXerxes: # condição desnecessária
        continue
    elif jogadaDario > 2:
        opcoes = opcoes[::-1]
        if opcoes.index(jogadaDario) < opcoes.index(jogadaXerxes):
            dario += 1
        else:
            xerxes += 1
    else:
        if opcoes.index(jogadaDario) < opcoes.index(jogadaXerxes):
            dario += 1
        else:
            xerxes += 1

if dario > xerxes:
    print("dario")
else:
    print("xerxes")

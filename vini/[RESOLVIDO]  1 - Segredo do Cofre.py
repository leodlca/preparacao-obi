firstLine = input("")
secondLine = input("")
thirdLine = input("")

nPosBarra = firstLine.split(" ")[0]
nPosSegr = firstLine.split(" ")[1]

barraNums = secondLine.split(" ")

seqPos = thirdLine.split(" ")

analisNum = []

posAtual = 0

for n in range(0, int(nPosSegr)):
    if n == 0:
        analisNum.append(int(barraNums[0]))
    if posAtual < (int(seqPos[n])):
        for i in range(posAtual + 1, int(seqPos[n])):
            analisNum.append(int(barraNums[i]))
    elif posAtual > (int(seqPos[n])):
        for i in range(int(seqPos[n]) - 1, (posAtual + 1)):
            analisNum.append(int(barraNums[i]))
    posAtual = int(seqPos[n]) - 1

resposta = ""

for n in range(0, 10):
    resposta += str(analisNum.count(n)) + " "
    
print(resposta)
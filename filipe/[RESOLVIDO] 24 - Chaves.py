# Tempo: 8min

linhas = []
chaveAberta = 0
chaveFechada = 0

limite = int(input())
count = 1

while limite >= count:
    linha = input()
    linhas.append(linha)
    count += 1

for linha in linhas:
    chaveAberta += linha.count("{")
    chaveFechada += linha.count("}")

if chaveAberta == chaveFechada:
    print("S")
else:
    print("N")

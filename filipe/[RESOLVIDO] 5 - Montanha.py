# Tempo: 8 min

numeros = int(input())
alturas = input()
alturas = list(alturas.replace(" ", ""))

doisPicos = False
for idx, altura in enumerate(alturas):
    if (idx > 0 and idx < len(alturas) - 1):
        if(alturas[idx - 1] > altura and alturas[idx + 1] > altura):
            doisPicos = True

print("S" if doisPicos else "N")

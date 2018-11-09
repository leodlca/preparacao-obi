cartas = list(int(x) for x in input().split())

cartasDecrescente = list(cartas)
cartasDecrescente.sort(reverse=True)

cartasCrescente = list(cartas)
cartasCrescente.sort()

if cartas == cartasCrescente:
    print("C")
elif cartas == cartasDecrescente:
    print("D")
else:
    print("N")

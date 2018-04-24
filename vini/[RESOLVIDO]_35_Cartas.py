cartas = [int(x) for x in input("").split(" ")]
copiaCartasO = [x for x in cartas]
copiaCartasD = [x for x in cartas]

copiaCartasO.sort()
copiaCartasD.sort(reverse=True)

if copiaCartasO == cartas:
    print("C")
elif copiaCartasD == cartas:
    print("D")
else:
    print("N")


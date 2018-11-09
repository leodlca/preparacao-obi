# 13min 42s
# Complexidade no pior caso é algo próximo de O(2*n^2), mas na maioria dos casos é logarítmica.

cartas = [int(x) for x in input("").split(" ")]
original_cartas = [x for x in cartas]

def output():
    cartas.sort()
    if cartas == original_cartas:
        return print("C")
    
    cartas.sort(reverse=True)
    if cartas == original_cartas:
        return print("D")

    return print("N")

output()
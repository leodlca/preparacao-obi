# 16min e 23s
# Complexidade quadrática O(n^2)

n_of_arrows = int(input())

arrowsXY = []

for i in range(0, n_of_arrows):
    formatted = [int(x) for x in input().split(" ")]
    arrowsXY.append({"x": formatted[0], "y": formatted[1], "distance_from_center": abs(formatted[0]) + abs(formatted[1])})

if n_of_arrows > 0:
    print("0")

counter = 0
for i in range(1, n_of_arrows):
    local_counter = 0
    for n in range(0, i):
        if arrowsXY[n]['distance_from_center'] <= arrowsXY[i]['distance_from_center']:
            local_counter += 1
        if local_counter > counter:
            counter = local_counter
    print(str(counter))
    
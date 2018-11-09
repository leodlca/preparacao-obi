_ = input()
caixas = [int(x) for x in input().split(' ')]

caixas.sort()

if(caixas[0] > 8):
    print('N')
else:
    for i in range(len(caixas)):
        if i == len(caixas) - 1:
            print('S')
            break
        elif abs(caixas[i] - caixas[i + 1]) > 8:
            print('N')
            break
    
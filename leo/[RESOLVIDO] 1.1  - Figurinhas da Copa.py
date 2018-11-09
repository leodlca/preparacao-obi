
row_1 = [int(x) for x in input().split(' ')]

n_figurinhas_totais = row_1[0]
n_figurinhas_carimbadas = row_1[1]
n_figurinhas_compradas = row_1[2]

figurinhas_carimbadas = [int(x) for x in input().split(' ')]
figurinhas_compradas = [int(x) for x in input().split(' ')]

for figurinha_carimbada in figurinhas_carimbadas:
    if figurinha_carimbada in figurinhas_compradas:
        n_figurinhas_carimbadas -= 1

print(n_figurinhas_carimbadas)
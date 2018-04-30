# < 3 min
# Complexidade linear O(2n), poderia ser reduzido pra O(n) mas o problema é muito simples.

n_of_inputs = int(input(""))

postes = [int(x) for x in input("").split(" ")]

print(str(len([x for x in postes if x < 50])) + ' ' + str(len([x for x in postes if x >= 50 and x < 85]))) 
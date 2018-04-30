# ~30min
# Complexidade ~O(n^2), provavelmente pode ser reduzida, mas o limite de casos é baixo (8).

n_of_cards = int(input())
copy_of_n_of_cards = n_of_cards
possibilities = 1

# fatorial
while copy_of_n_of_cards > 1:
    possibilities *= copy_of_n_of_cards
    copy_of_n_of_cards -= 1

input_combinations = []
my_calculation = {}

for i in range(0, possibilities - 1):
    input_combinations.append([int(x) for x in input().split(" ")])
    if i < n_of_cards: my_calculation[str(i + 1)] = []

for out_idx in range(0, len(input_combinations)):
    for in_idx in range(0, len(input_combinations[out_idx])):
        my_calculation[str(in_idx + 1)].append(input_combinations[out_idx][in_idx])

answer = []

def print_item_that_occurs_less(arr):
    item_that_occurs_less = 0
    how_many_occurrencies = possibilities
    for i in range(1, n_of_cards + 1):
        occurrencies = arr.count(i)
        if occurrencies < how_many_occurrencies:
            item_that_occurs_less = i
            how_many_occurrencies = occurrencies
    print(item_that_occurs_less, end=' ')

for n_card in range(1, n_of_cards + 1):
    print_item_that_occurs_less(my_calculation[str(n_card)])


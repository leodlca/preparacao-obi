# 32min 23s
# Complexidade linear + quadrático próxima de O(n) + O(n^2), ainda não consegui reduzir o algorítmo quadrático, por isso o erro de timeout pra casos grandes.

# Passa em 40% dos casos, em que N e M <= 100, no resto, em que N e M <= 1000, dá erro de timeout.

first_row = [int(x) for x in input("").split(" ")]

bar_size = first_row[0]
how_many_moves = first_row[1]

bar = [int(x) for x in input("").split(" ")]
moves = [int(x) for x in input("").split(" ")]

passkey = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def perform_move(current_position, intended_position):
    counting_moves = 0
    while current_position != intended_position:

        passkey_index = bar[current_position-1]
        passkey[passkey_index] += 1
        current_position = add_or_subtract(current_position, intended_position)
        counting_moves += 1

    return current_position

def add_or_subtract(current_position, intended_position):
    if current_position > intended_position:
        return current_position - 1
    else:
        return current_position + 1

def print_result():
    print(' '.join([str(x) for x in passkey]))

def main():
    current_position = moves[0]
    for move in moves:
        current_position = perform_move(current_position, move)
    passkey[bar[current_position - 1]] += 1
    print_result()

main()

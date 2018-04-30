# 7min e 5s
# Complexidade constante O(1)

user_input = [int(x) for x in input().split(" ")]

actual_state = [user_input[0], user_input[1]]
wanted_state = [user_input[2], user_input[3]]

if actual_state == wanted_state: # as lampadas já estão como deveriam
    print("0")
elif actual_state[0] == wanted_state[0]: # lâmpada A tá certa e a B não, vai precisar mudar as duas e mudar a A de novo, 2 movimentos.
    print("2")
else: # as duas estão diferentes, ou apenas o A está diferente, é só apertar um botão 1 movimento.
    print("1")
    
# 7min 41s
# Complexidade linear O(n)

n_of_inputs = int(input(""))

plays = []

for i in range(0, n_of_inputs):
    user_input = input("").split(" ")
    plays.append({"dario": int(user_input[0]), "xerxes": int(user_input[1])})

dario = 0
xerxes = 0

for play in plays:
    if play["dario"] == 0:
        if play["xerxes"] == 1:
            dario += 1
        elif play["xerxes"] == 2:
            dario += 1
        elif play["xerxes"] == 3:
            xerxes += 1
        elif play["xerxes"] == 4:
            xerxes += 1
    elif play["dario"] == 1:
        if play["xerxes"] == 0:
            xerxes += 1
        elif play["xerxes"] == 2:
            dario += 1
        elif play["xerxes"] == 3:
            dario += 1
        elif play["xerxes"] == 4:
            xerxes += 1
    elif play["dario"] == 2:
        if play["xerxes"] == 0:
            xerxes += 1
        elif play["xerxes"] == 1:
            xerxes += 1
        elif play["xerxes"] == 3:
            dario += 1
        elif play["xerxes"] == 4:
            dario += 1
    elif play["dario"] == 3:
        if play["xerxes"] == 0:
            dario += 1
        elif play["xerxes"] == 1:
            xerxes += 1
        elif play["xerxes"] == 2:
            xerxes += 1
        elif play["xerxes"] == 4:
            dario += 1
    elif play["dario"] == 4:
        if play["xerxes"] == 0:
            dario += 1
        elif play["xerxes"] == 1:
            dario += 1
        elif play["xerxes"] == 2:
            xerxes += 1
        elif play["xerxes"] == 3:
            xerxes += 1

if dario > xerxes:
    print("dario")
else:
    print("xerxes")
first_row = input()
second_row = input()

allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

first = ''
dot = False
dot_count = 0
for char in first_row:
    if not dot and char == '.':
        first += char
        dot = True
    elif char in allowed:
        if dot:
            dot_count += 1
        first += char
        if dot_count == 2:
            break

cpf = first[:11]
first = float(first[11:])

second = ''
dot = False
dot_count = 0
for char in second_row:
    if not dot and char == '.':
        second += char
        dot = True
        print(dot)
    elif char in allowed:
        if dot:
            dot_count += 1
        second += char
        if dot_count == 2:
            break

second = float(second)



print('cpf ' + cpf)
print(round(first + second, 2))
# 4min 50s
# Complexidade constante O(1) 

user_input = []

for i in range(0, 3):
    user_input.append(int(input("")))

n_of_positions = user_input[0]
enemy_position = user_input[1]
player_position = user_input[2]

if enemy_position >= player_position:
    result = enemy_position - player_position
else:
    result = (n_of_positions - player_position) + enemy_position

print(result)
# 37min 26s

import math

number_of_inputs = int(input(""))

formatted_input = []
count = 0

for i in (range(0, number_of_inputs)):
    str_input = input("")
    splitted_input = str_input.split(" ")
    formatted_input.append({"size": splitted_input[0], "side": splitted_input[1]})

for i in formatted_input:
    same_size_arr = list(filter(lambda x: x['size'] == i['size'], formatted_input))
    left_arr = list(filter(lambda x: x['side'] == 'E', same_size_arr))
    right_arr = list(filter(lambda x: x['side'] == 'D', same_size_arr))
    left_len = len(left_arr)
    right_len = len(right_arr)

    smaller_len = left_len if left_len < right_len else right_len
    count += smaller_len

    formatted_input = list(filter(lambda x: x['size'] != i['size'], formatted_input))

print(count)
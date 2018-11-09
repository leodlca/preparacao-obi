# < 2min
# Complexidade O(1)

import math

first_line = input().split(" ")

n_of_subjects = int(first_line[0])
n_of_pages = int(first_line[1])

pages_per_subject = [int(x) for x in input().split(" ")]
total_pages = sum(pages_per_subject)

answer = str(math.ceil(total_pages / n_of_pages))

print(answer)
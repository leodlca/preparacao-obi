# 3min 02s
# Complexidade linear O(n)

number = int(input(''))
divisor = 1.0
answer = 0

while divisor <= number:
    if (number / divisor) % 1 == 0:
        answer += 1
    divisor += 1.0

print(answer)

inputs = []

while True:
    line = input()
    if line == '': break
    inputs.append([int(x) for x in line.split(" ")])

def threeplusone(n):
    counter = 1
    while n != 1:
        counter += 1
        if n % 2.0 != 0:
            n = 3*n + 1
        else:
            n = n/2
    return counter

def main():
    for index, number_pair in enumerate(inputs):
        highest = 0
        if number_pair[0] > number_pair[1]:
            maior = number_pair[0]
            menor = number_pair[1]
        else:
            maior = number_pair[1]
            menor = number_pair[0]

        for i in range(menor, maior + 1):
            current = threeplusone(i)
            if current > highest:
                highest = current
        inputs[index].append(highest)

def print_nicely():
    for number_trial in inputs:
        print(' '.join([str(x) for x in number_trial]))

main()
print_nicely()
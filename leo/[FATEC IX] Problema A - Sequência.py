t_esimo = int(input())

sequence = [2, 2, 2, 2, 2]

if t_esimo < 5:
  print(2)
else:
  for i in range(5, t_esimo + 1):
    to_be_summed = [sequence[i-1], sequence[i-2], sequence[i-3], sequence[i-4], sequence[i-5]]
    sequence.append(sum(to_be_summed))
  print(sequence[t_esimo])
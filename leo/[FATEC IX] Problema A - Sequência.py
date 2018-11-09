n = int(input())

arr = [2, 2, 2, 2, 2]

if n <= 5:
	print(2)
	exit()
for i in range(5, n+1):
	_sum = sum(arr[i-5:i])
	if i == n:
		print(_sum)
		exit()
	else:
		arr.append(_sum)

import math

def comp(x, b):
	ret = 0
	while x:
		ret = ret * b + (x & 1)
		x //= 2
	return ret

def find(n):
	i = 2
	while (i < n and i < 20):
		if (n % i == 0):
			return i
		i += 1
	return 1

t = int(input())
a, b = map(int, input().split())
sol = 0
print("Case #1:")
for i in range(2**(a-1) + 1, 2**a + 1, 2):
	if (sol == b):
		break
	v = []
	flag = True
	for j in range(2, 11):
		n = comp(i, j)
		div = find(n)
		if (div == 1):
			flag = False
		v.append(div)
	if (flag == True):
		sol += 1
		x = i
		while x:
			print(int(x) & 1, end='')
			x //= 2
		print(end=' ')
		for j in v:
			print(j, end=' ')
		print('')

		


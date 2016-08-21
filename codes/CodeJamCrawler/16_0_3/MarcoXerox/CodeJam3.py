input()
from math import sqrt
n,j = map(int, input().split())
base = [[b**i for i in range(n)] for b in range(2, 10+1)]
def prod(x):
	if not x%2:
		return 2
	for k in range(3,int(sqrt(x))+2,2):
		if not x%k:
			return k
	return 1
print("Case #1:")
for x in range(2**n//2, 2**n):
	binary = bin(x)[2:]
	if binary[-1] != '1':
		continue
	if not j:
		break
	v = list()
	for b in range(2, 10+1):
		s = sum(dx*dy for dx,dy in zip(map(int, reversed(binary)),base[b-2]))
		v.append(prod(s))
	if 1 in v:
		continue
	print(binary, ' '.join(map(str, v)))
	j -= 1

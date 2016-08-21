n = int(input())
for i in range(n):
	K, C, S = [int(x) for x in input().split()]
	print("Case #{0}:".format(i+1),end='')
	for j in range(S):
		print(" {0}".format(1+j*K**(C-1)),end='')
	print()
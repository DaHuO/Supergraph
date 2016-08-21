'''input
5
0
1
2
11
1692
'''
for T in range(int(input())):
	N = int(input())

	digits = set([x for x in range(10)])

	num = 0
	if N > 0:
		while len(digits) > 0:
			num += N
			digits -= set([int(x) for x in str(num)])

	print("Case #{}: {}".format(T+1, num if num else "INSOMNIA"))
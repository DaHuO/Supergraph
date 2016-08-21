'''input
5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3
'''
for T in range(int(input())):
	K, C, S = map(int, input().split())

	res = ""
	if K == 1:
		res = "1"
	elif S < K:
		res = "IMPOSSIBLE"
	else:
		res = " ".join([str(x) for x in range(1 if C == 1 else 2, K + 1)])

	print("Case #{}: {}".format(T+1, res))


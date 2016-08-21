'''input
1
26
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
'''
for T in range(int(input())):
	N = input()
	P = list(map(int, input().split()))

	#print(P)
	i = 0

	print("Case #{}: ".format(T+1), end="")

	group = []
	while sum(P) > 0 and i < 1000:
		i += 1

		k = P.count(max(P))
		if k == 2:
			a = P.index(max(P))
			P[a] -= 1
			b = P.index(max(P))
			P[b] -= 1
			group.append(chr(ord('A') + a))
			group.append(chr(ord('A') + b))
		elif k > 2:
			a = P.index(max(P))
			P[a] -= 1
			group.append(chr(ord('A') + a))
		elif k == 1:
			a = P.index(max(P))
			P[a] -= 1
			group.append(chr(ord('A') + a))

		#print(P)
		if P.count(max(P)) <= 2 or len(group) == 2:
			print("".join(group), end="")
			print(" ", end="")
			group = []
		#print(P)


	if len(group) > 0:
		print("".join(group), end="")
		print(" ", end="")

	print()
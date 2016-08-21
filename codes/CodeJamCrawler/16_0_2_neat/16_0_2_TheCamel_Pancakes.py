T = int(input())
for case in range(1,T+1):
	S = input()
	n = len(S)

	res = 0
	obj = '+'*n

	found = (S == obj)

	treated = set()
	queue = [S]

	while not found:
		newQueue = []
		for pos in queue:
			if pos == obj:
				found = True
				break
			else:
				for i in range(0,n):
					inv = list(map(lambda x: '-' if x=='+' else '+', pos[i::-1]))
					newPos = ''.join(inv + list(pos[i+1:]))
					if newPos in treated or newPos in newQueue:
						continue
					else:
						newQueue.append(newPos)
			treated.add(pos)
		queue = newQueue
		if not found:
			res += 1

	print("Case #", case, ": ", res, sep="")
for _ in range(int(input())):
	answer = 0
	s = input()
	d = [c == '+' for c in s]
	while not all(d):
		answer += 1
		if d[0]:
			for i in range(d.index(False)): d[i] = False
		else:
			if any(d):
				for i in range(d.index(True)): d[i] = True
			else: d = [not x for x in d[::-1]]
	print("Case #" + str(_ + 1) + ": " + str(answer))

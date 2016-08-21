for _ in range(int(input())):
	i = int(input())
	if i == 0: answer = "INSOMNIA"
	else:
		answer = 0
		seen = []
		k = 1
		while answer == 0:
			s = str(k * i)
			for c in s:
				if c not in seen:
					seen.append(c)
					if len(seen) == 10:
						answer = k * i
			k += 1
	print ("Case #" + str(_ + 1) + ": " + str(answer))
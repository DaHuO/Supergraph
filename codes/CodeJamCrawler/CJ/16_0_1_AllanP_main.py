x = int(input())
for i in range(x):
		res = []
		y = input()
		c = int(y)
		aux = 1
		c1 = 0
		while not(len(res) == 10):
			c1 = c * (aux)
			if c1 == 0:
				break
			y = str(c1)
			for j in y:
				if res.count(j) == 0:
					res.append(j)
			aux = aux + 1
		if len(res) == 10:
			print ("Case #" + str(i + 1) + ": " + str(y))
		else:
			print ("Case #" + str(i + 1) + ": INSOMNIA")


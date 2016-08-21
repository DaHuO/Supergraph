a = open("a.in", 'r')
answer = open("answer_a_big.txt", 'w')

n = int(a.readline().strip())

for i in range(n):
	c = set()
	num = int(a.readline().strip())
	l = 1
	y = set()
	while True:
		u = str(l*num)
		k = set(u)
		y.update(k)
		
		if len(y) == 10:
			break
		if l > 100000:
			u = "INSOMNIA"
			break
		l += 1
		
	answer.write("Case #" + str(i+1) + ": " + u + "\n")
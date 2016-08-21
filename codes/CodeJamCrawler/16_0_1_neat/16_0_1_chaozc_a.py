from sys import argv
if __name__ == "__main__":
	inf = open(argv[1], 'r')
	lines = inf.readlines()
	inf.close()
	dic = {}
	T = int(lines[0][:-1])
	ouf = open(argv[2], 'w')
	for i in range(1, T+1):
		N = int(lines[i][:-1])
		for j in range(10):
			dic[j] = False
		cnt = 10
		for j in range(100):
			M = N*(j+1)
			while (M > 0):
				p = M%10
				if not(dic[p]):
					cnt -= 1
					dic[p] = True
				M /= 10
			if cnt == 0:
				ouf.write("Case #%d: %d\n"%(i, N*(j+1)))
				break
		if cnt > 0:
			ouf.write("Case #%d: INSOMNIA\n"%(i))
	ouf.close()
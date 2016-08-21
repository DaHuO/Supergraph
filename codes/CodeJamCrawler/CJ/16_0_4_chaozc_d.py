from sys import argv
if __name__ == "__main__":
	inf = open(argv[1], 'r')
	lines = inf.readlines()
	inf.close()
	T = int(lines[0][:-1])
	ouf = open(argv[2], 'w')
	for l in range(1, T+1):
		ouf.write("Case #%d: "%(l))
		line = lines[l][:-1]
		para = line.split(' ')
		K, C, S = int(para[0]), int(para[1]), int(para[2])
		minS = K if C == 1 else K-1
		if S < minS:
			ouf.write("IMPOSSIBLE\n")
		else:
			alist = [str(i) for i in range(2 if C > 1 else 1, K+1)]
			ans = " ".join(alist)
			if K == 1:
				ouf.write("1 \n")
			else:
				ouf.write(ans+"\n")
	ouf.close()
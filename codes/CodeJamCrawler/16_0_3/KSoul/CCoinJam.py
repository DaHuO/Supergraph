import sys

def checkprime(x):
	i = 2
	while i*i < x:
		if x % i == 0:
			return False, i
		i = i + 1
	return True, 0

def coin_jam(argv):
	powerxy = [[1],[1],[1],[1],[1],[1],[1],[1],[1]]
	with open(argv[0], 'r') as f:
		t = int(f.readline())
		for i in range(t):
			n, j = f.readline().strip().split()
			for idx, x in enumerate(powerxy):
				for y in range(1,32):
					x.append((idx+2)*x[y-1])
			allbit = ["0","1"]
			l = 0
			while l < int(n)-1-2:
				temp = allbit
				allbit = []
				for x in temp:
					allbit.append(x+"0")
					allbit.append(x+"1")
				l = l + 1
			allnum = ["1" + x + "1" for x in allbit]
			print "Case #1:"
			sol = []
			for i in allnum:
				solbase = []
				for base in powerxy:
					if i not in allnum:
						break
					numinbase = sum([int(x)*base[int(n)-idx-1] for idx, x in enumerate(i)])
					is_prime, divisor = checkprime(numinbase)
					solbase.append(str(divisor))
					if is_prime == True:
						allnum.remove(i)
				if i in allnum:
					sol.append((i, solbase))
					if len(sol) >= int(j):
						break
			for i in sol:
				print i[0], " ".join(i[1])
					




if __name__ == "__main__":
	coin_jam(sys.argv[1:])
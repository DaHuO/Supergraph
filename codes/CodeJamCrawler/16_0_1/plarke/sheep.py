infile = 'A-large.in'
outfile = "A-large.out"

def trials(n):
	if n == 0:
		return "INSOMNIA"
	else:
		i = 0
		seen = set()
		while len(seen) < 10:
			i += 1
			seen |= set(str(i*n))
		return str(i*n)

def solve():
	with open(infile, 'r') as f, open(outfile, 'w+') as out:
		T = int(f.readline())
		print(T)
		for i in range(T):
			N = int(f.readline())
			ans = trials(N)
			out.write("Case #{0}: {1}\n".format(i +1, ans))

if __name__ == '__main__':
	solve()
		

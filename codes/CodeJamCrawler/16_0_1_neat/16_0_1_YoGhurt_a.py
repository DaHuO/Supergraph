def solve(n, x, res):
	if n == 0:
		res.write("Case #{}: INSOMNIA\n".format((x+1)))
	else:
		i = 0
		a = [False, False, False, False, False, False, False, False, False, False]
		while False in a:
			i += n
			i = str(i)
			for c in i:
				a[ord(c) - ord('0')] = True
			i = int(i)
		res.write("Case #{}: {}\n".format((x+1), i))

def main():
	f = open("C://CodeJam/large.in", 'r')
	res = open("C://CodeJam/alarge.out", 'w')
	T = int(f.readline())
	for x in range(T):
		N = int(f.readline())
		solve(N, x, res)
	f.close()
	res.close()	

if __name__ == "__main__":
	main()
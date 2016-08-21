def solve(n):
	seen = [0]*10
	a = 0
	for i in range(10000):
		a += n
		x = str(a)
		for char in x:
			if seen[int(char)] == 0:
				seen[int(char)] = 1
		if(sum(seen)==10):
			return str(a)
	else:
		return 'INSOMNIA'

if __name__=="__main__":
	ip = open('small.in')
	out = open('small.out','w')
	cases = int(ip.readline())
	for i in range(1,cases+1):
		x = solve(int(ip.readline()))
		out.write('Case #'+str(i)+': '+x+'\n')
	ip.close()
	out.close()

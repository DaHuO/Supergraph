def solve(k, c, s, x, res):
	l = []
	for j in range(k):
		l.append(str(j + 1))
	s = " ".join(l)
	res.write("Case #{}: {}\n".format((x+1), s))

def main():
	f = open("C://CodeJam/d.in", 'r')
	res = open("C://CodeJam/d.out", 'w')
	T = int(f.readline())
	for x in range(T):
		s = f.readline()
		ss = s.split()
		k = int(ss[0])
		c = int(ss[1])
		s = int(ss[2])
		solve(k, c, s, x, res)
	f.close()
	res.close()	

if __name__ == "__main__":
	main()
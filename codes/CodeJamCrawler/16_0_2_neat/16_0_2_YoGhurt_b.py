def solve(s, x, res):
	pm = s.count("+-")
	result = pm * 2
	if s[0] == "-":
		result += 1
	res.write("Case #{}: {}\n".format((x+1), result))

def main():
	f = open("C://CodeJam/blarge.in", 'r')
	res = open("C://CodeJam/blarge.out", 'w')
	T = int(f.readline())
	for x in range(T):
		s = f.readline()
		solve(s, x, res)
	f.close()
	res.close()	

if __name__ == "__main__":
	main()
def solve(N):
	if N == 0:
		return "INSOMNIA"
	digits = set([])
	curr = N
	while True:
		n = str(curr)
		for i in n:
			digits.add(i)
		if(len(digits) == 10):
			return curr;
		curr += N;
	return "INSOMNIA"

fin = open("A-large.in")
fout = open("output.txt", "w");

line = fin.readline()
T = int("".join(line.split()))
for i in range(T):
	line = fin.readline()
	N = int("".join(line.split()))
	ans = solve(N);
	print "Case #"+str(i+1)+": "+str(ans)
	fout.write("Case #"+str(i+1)+": "+str(ans)+"\n")

fin = open("D-small-attempt0.in", "r")
fout = open("output.txt", "w")

t = int(fin.readline())
for case in xrange(1,t+1):
	k,c,s = map(int, fin.readline().split())
	lb = "" if case == t else "\n"
	fout.write("Case #" + str(case) + ": " + " ".join([str(i) for i in xrange(1,s+1)]) + lb)
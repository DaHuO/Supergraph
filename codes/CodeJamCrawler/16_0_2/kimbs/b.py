import sys

def solve(case, seq):
	cnt = 0
	if seq[0] == '-' :
		cnt = -1

	flag = False
	for i in range(len(seq)) :
		if seq[i] == '-' :
			if not flag :
				flag = True
				cnt += 2
		else :
			flag = False

	return "Case #%d: %d\n" % (case, cnt)

f = open("B-large.in")
#rl = lambda: sys.stdin.readline()
rl = lambda: f.readline()
T = int(rl())

output = open("output.txt", 'w')

for i in range(T):
	seq = str(rl())
	out = solve(i + 1, seq)
	print out
	output.write(out)


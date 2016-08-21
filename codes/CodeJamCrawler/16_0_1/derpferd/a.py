import sys

def put(s):
	sys.stdout.write(s)

sys.stdin = open("a.in", "r")
sys.stdout = open("a.out", "w")

for t in range(int(raw_input())):
	put("Case #" + str(t+1) + ": ")
	seen = set()
	n = int(raw_input())
	i = 0
	if n == 0:
		put("INSOMNIA\n")
		continue
	while len(seen) != 10:
		i += 1
		seen |= set([x for x in str(i*n)])
	put(str(i*n) + "\n")

sys.stdout.close()
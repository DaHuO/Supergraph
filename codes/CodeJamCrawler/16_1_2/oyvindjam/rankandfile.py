import sys

test_cases = int(sys.stdin.readline())

f = open("output", "w")

for i in range(0, test_cases):
	N = int(sys.stdin.readline())
	lists = []
	for j in range(0, N * 2 - 1):
		lists.extend([int(x) for x in sys.stdin.readline().strip().split(" ")])
	
	numbers = set(lists)
	missing = []
	for n in numbers:
		if (lists.count(n) % 2) != 0:
			missing.append(n)
	
	f.write("Case #%d: %s\n" % (i + 1, " ".join(str(x) for x in sorted(missing))))

f.close()


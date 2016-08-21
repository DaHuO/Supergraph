import sys

def solve(case, N):
	s = set([])

	result = "INSOMNIA"

	if N != 0 :
		i = 1

		while True :
			n = i * N
			while n > 0 :
				s.add(n % 10)
				n = int(n / 10)

			if len(s) == 10 :
				result = i * N
				break
			i = i + 1

	return "Case #%d: %s\n" % (case, result)

f = open("A-large.in")
#rl = lambda: sys.stdin.readline()
rl = lambda: f.readline()
T = int(rl())

output = open("output.txt", 'w')

for i in range(T):
	n = int(rl())
	out = solve(i + 1, n)
	output.write(out)


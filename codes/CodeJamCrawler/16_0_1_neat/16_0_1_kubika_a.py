from __future__ import division

f = open("A-large.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0

for i in range(cases):
	n = int(f.readline())

	if n == 0:
		result = "INSOMNIA"
	else:
		result = 1
		digits = []
		while len(digits) < 10:
			digits = set(list(digits) + list(str(result*n)))
			result = result + 1 
			print digits
		result = (result - 1) * n
		print digits

	g.write("Case #" + str(i + 1) + ": " + str(result) +  "\n")

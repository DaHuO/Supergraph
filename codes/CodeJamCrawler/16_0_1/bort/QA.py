import sys

def solve(n):
	digits = set({})
	N = int(n)
	m = 1

	while True:
		current = len(digits)

		for i in range(10000):
			for c in str(m * N): 
				#print(c, digits)
				digits.add(c)
			if len(digits) == 10:
				return str(m * N)
			else:
				m += 1
				#print m * N

		if len(digits) == current:
			return "INSOMNIA"



with open('A-large.in') as f, open('A-large.out', 'w') as o:
	lines = f.readlines()

	case = 1
	for line in lines[1:]:
		o.write("Case #{0}: {1}\n".format(case, solve(line)))
		case += 1
	
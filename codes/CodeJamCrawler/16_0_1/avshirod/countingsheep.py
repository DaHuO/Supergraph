import sys

# no_of_inputs = int(sys.argv[1])
with open('A-large.in', 'r') as inp:
	lines = inp.readlines()
	no_of_inputs = int(lines[0])
	inputs = []
	for i in range(1, no_of_inputs+1):
		#inputs.append(int(sys.argv[i+1]))
		inputs.append(int(lines[i].strip()))

def update(n, check, m):
	n = (m+1) * n
	for i in range(10):
		if check[i] == 0:
			if str(i) in str(n):
				check[i] = 1
	return check

with open('A-big-attempt0.out', 'w') as out:
	for i,num in enumerate(inputs, start=1):
		int_appear = [0] * 10
		answer = "INSOMNIA"
		multiplier = 0
		if num != 0:
			while sum(int_appear) != 10:
				int_appear = update(num, int_appear, multiplier)
				multiplier += 1
		if sum(int_appear) == 10:
			answer = num * multiplier
		out.write("Case #%d: %s" % (i, answer))
		out.write("\n")
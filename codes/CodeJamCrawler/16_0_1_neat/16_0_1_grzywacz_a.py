import sys

def solve(n):
	if n == 0:
		return "INSOMNIA"
		
	all_digits = set("0123456789")
	i = 1
	while True:
		digits = set(str(n*i))
		all_digits.difference_update(digits)
		if not all_digits:
			return n*i
		else:
			i += 1
			
if __name__ == '__main__':
	idx = 1
	input = open(sys.argv[1])
	output = open(sys.argv[1] + '.out', 'w')
	T = input.readline()
	for n in input:
		answer = solve(int(n))
		output_line = "Case #%d: %s" % (idx, answer)
		print output_line
		output.write(output_line + "\n")
		idx += 1
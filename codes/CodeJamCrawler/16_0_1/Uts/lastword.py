T = int(raw_input())

def solve(input):
	output = input[0]
	for c in input[1:]:
		if c >= output[0]:
			output = c + output
		else:
			output = output + c
	return output

for t in range(1, T+1):
	print "Case #%d: %s" % (t, solve(raw_input()))
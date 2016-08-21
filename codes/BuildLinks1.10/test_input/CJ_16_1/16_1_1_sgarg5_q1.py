import sys

def get_string(input):
	op = [input[0]]
	for i in xrange(1, len(input)):
		if input[i] >= op[0]:
			op[:0] = input[i]
		else:
			op.append(input[i])
	return ("").join(op)

t = input()
for i in range(t):
	input_str = raw_input()
	print "Case #%d: %s" %(i+1, get_string(input_str))
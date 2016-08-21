def rev(part):
	return part[::-1]

def flip(seq):
	for i in xrange(len(seq)):
		seq[i] = '-' if seq[i] == '+' else '+'
	return seq

def solve(sequence):
	if len(sequence) == 1:
		return 0 if sequence[0] == '+' else 1

	sequence = list(sequence)
	count = 0
	i = 0	
	while i < len(sequence) - 1:
		if sequence[i] != sequence[i+1]:
			sequence = rev(flip(sequence[:i+1])) + sequence[i+1:]
			count += 1											     
		i += 1

	if sequence[0] == '-':
		count += 1

	return count

for t in xrange(1, input()+1):
	sequence = raw_input()
	print "Case #{0}: {1}".format(t, solve(sequence))
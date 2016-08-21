import sys

def answer(x):
	# if 0, return insomnia
	if x == 0:
		return 'INSOMNIA'
	# otherwise, loop through, tracking new digits
	seen = {'0': False,
		    '1': False,
		    '2': False,
		    '3': False,
		    '4': False,
		    '5': False,
		    '6': False,
		    '7': False,
		    '8': False,
		    '9': False}
	seen_count = 0
	m = 1
	curr_num = 0
	while seen_count < 10: 
		curr_num = x*m
		curr_string = "{}".format(curr_num)
		m += 1
		for c in curr_string:
			if not seen[c]:
				seen[c] = True
				seen_count += 1
	return curr_num

data = sys.stdin
i = 1
for line in data.readlines()[1:]:
	print "Case #{}: {}".format(i, answer(int(line)))
	i += 1
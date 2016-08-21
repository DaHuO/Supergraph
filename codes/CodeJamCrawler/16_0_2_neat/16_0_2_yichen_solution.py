def h(sign):
	return sign == '+'

def reverse(sign):
	if sign == '+':
		return '-'
	else:
		return '+'

def flip(lst):
	lst.reverse()
	return list(map(reverse, lst))

def best(inputs):
	if len(inputs) == 1:
		if h(inputs[0]):
			return 0
		else:
			return 1
	else:
		if h(inputs[-1]):
			return best(inputs[:-1])
		else:
			if h(inputs[0]):
				return 1 + best(list(map(reverse, inputs))[:-1])
			else:
				return 1 + best(flip(inputs)[:-1])


def solve(case_number):
	inputs = [s for s in raw_input()]
	ans = best(inputs)
	print "Case #{}: {}".format(case_number, ans)

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)

'''
python solution.py <small.in> small.out
python solution.py <large.in> large.out
'''
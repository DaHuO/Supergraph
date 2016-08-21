T = int(raw_input())

def replace(s):
	ret = ""
	for each in reversed(s):
		if  each == "-":
			ret += "+"
		else:
			ret += "-"
	return ret

memo_count = {}
memo_value = {}

def swap(s):
	if s == "+":
		return "-"
	return "+"


for t in range(T):
	s = raw_input()
	# print "-----------"
	
	current = s[0]
	count = 0
	for i in xrange(1,len(s)):
		if s[i] != current:
			current = swap(current)
			count += 1
	if current == "-":
		count += 1
	print "Case #%d: %d" % ( t+ 1, count)
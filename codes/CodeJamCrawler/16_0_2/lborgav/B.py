
def process_string(st):
	first = st[0]
	flips = 0
	for i in xrange(len(st)-1):
		if st[i+1] == st[i]: pass
		else: flips += 1
	if flips % 2 == 0:
		if first == '-':
			flips += 1
	else:
		if first == '+':
			flips += 1
	return flips

def main():
	T = raw_input()
	for i in xrange(int(T)):
		N = raw_input()
		flips = process_string(str(N))
		print "Case #%d: %d" % (i+1, flips)

main()

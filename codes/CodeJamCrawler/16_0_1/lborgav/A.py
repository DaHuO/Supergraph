
def split_to_list(n):
	return list(n)

def sheep(N):
	l = split_to_list(N)
	s = set(l)
	for i in xrange(2, 1000000):
		new_set = set(split_to_list(str(i*int(N))))
		s = s.union(new_set)
		if len(s) == 10:
			return i*int(N)
	return -1

def main():
	T = raw_input()
	for i in xrange(int(T)):
		N = raw_input()
		last_number = sheep(str(N))
		if last_number !=  -1:
			print "Case #%d: %d" % (i+1, last_number)
		else:
			print "Case #%d: %s" % (i+1, "INSOMNIA")

main()

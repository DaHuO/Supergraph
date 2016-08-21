#!usr/bin/python


def unique(s):
	st = set(s)
	return list(st)

t = int(raw_input())
for i in xrange(1, t+1):
	n = int(raw_input())
	if (n == 0):
		print "Case #{}: INSOMNIA".format(i)
	else:
		ls = unique(list(str(n)))
		if len(ls) == 10:
			print "Case #{}: {}".format(i, n)
		else:
			x = 1
			while (len(ls) != 10):
				m = x*n
				x = x + 1
				ls.extend(list(str(m)))
				ls = unique(ls)
			print "Case #{}: {}".format(i, m)

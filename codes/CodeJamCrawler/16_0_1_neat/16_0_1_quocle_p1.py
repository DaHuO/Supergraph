import sys
f = open(sys.argv[1], 'r')
N = int(f.readline().strip())
d = {}
for case in xrange(1, N+1):
	n = int(f.readline().strip())
	print 'Case #%s:' %(case),
	if n == 0:
		print 'INSOMNIA'
	else:
		d.clear()
		val = 0
		while True:
			val += n
			tmp = val
			while tmp > 0:
				digit = tmp %10
				if digit not in d:
					d[digit] = True
				tmp = tmp/10
			if len(d) == 10:
				print val
				break

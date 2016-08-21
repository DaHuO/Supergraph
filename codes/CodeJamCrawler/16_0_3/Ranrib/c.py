import sys
import time

def check_num(num):
	dividers = []
	for base in xrange(2,11):
		start = time.time()
		base_num = int(num, base)
		divided = False
		for i in xrange(2, 4294967295):
			if base_num % i == 0:
				dividers.append(i)
				divided = True
				break
			if time.time() - start > 1:
				return []
		if not divided:
			return []
	return dividers
		

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		N, J = lines.pop(0).strip().split()
		N = int(N) - 2
		J = int(J)
		print 'Case #%d:' % (i + 1)
		outfile.write('Case #%d:\n' % (i + 1))
		start_num = 0
		for j in xrange(J):
			divs = []
			num = None
			
			for x in xrange(start_num, 2**N):
				num = '1' + bin(x)[2:].rjust(N, '0') + '1'
				print num
				divs = check_num(num)
				if len(divs) != 0:
					start_num = x + 1
					break
			print '%s %s' % (num, ' '.join([str(x) for x in divs]))
			outfile.write('%s %s\n' % (num, ' '.join([str(x) for x in divs])))
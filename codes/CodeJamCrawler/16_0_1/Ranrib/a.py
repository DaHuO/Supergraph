import sys

def solve(num):
	if num == 0:
		return 'INSOMNIA'
	not_seen = range(0, 10)
	cur = num
	for i in xrange(1, 1001):
		cur = i * num
		while cur:
		    digit = cur % 10
		    if digit in not_seen:
		    	not_seen.remove(digit)
		   	if len(not_seen) == 0:
		   		return i*num
		    cur //= 10
	return 'INSOMNIA'
		

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		outfile.write('Case #%d: %s\n' % (i + 1, solve(int(lines.pop(0)))))
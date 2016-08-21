import sys

cache = dict()

def solve(stack, start, end):
	res = cache.get((start, end))
	if res is not None:
		return res
	
	total = -1
	no_need = "-" not in stack[start:end]
	
	if no_need:
		cache[(start, end)] = 0
		#print "1", stack[start:end], cache[(start, end)]
		return 0
	if start - end == 1:
		cache[(start, end)] = 1
		#print "2", stack[start:end], cache[(start, end)]
		return 1
	if "+" not in stack[start:end]:
		cache[(start, end)] = 1
		#print "3", stack[start:end], cache[(start, end)]
		return 1

	for i in xrange(start + 1, end):
		left = solve(stack, start, i) 
		right = solve(stack, i, end)
		
		if right > 0:
			right += 1
		new_total = left + right
		if total == -1 or total > new_total:
			total = new_total
	
	cache[(start, end)] = total
	#print stack[start:end], cache[(start, end)]
	return total
	
T = int(sys.stdin.readline())

for testcase in xrange(1, T + 1):
	stack = sys.stdin.readline().strip()
	cache = dict()
	ans = solve(stack, 0, len(stack))
	print "Case #%d: %d" % (testcase, ans)

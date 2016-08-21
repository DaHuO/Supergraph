from Queue import *

def flip(l):
    if l == "+":
        return "-"
    return "+"

def m(o, c):
	order = list(o)
	if (c == 0):
		return order
	for i in xrange(c/2 if c % 2 == 0 else c/2+1):
		order[i], order[c-i-1] = flip(order[c-i-1]), flip(order[i])
	return order

def isleaf(order):
    if not '-' in order:
        return True
    return False

def sBFS(s):
	l = list(s)

	q = Queue()
	q.put(l)

	dq = Queue()
	dq.put(1)

	depth = 0

	memo = {}
	memo[s] = 1
	if isleaf(l):
		return depth
	else:
		while not q.empty():
			d = q.get()
			depth = dq.get()
			#print depth
			for x in xrange(len(d)+1):
				c = m(d, x)
				if not ''.join(c) in memo:
					q.put(c)
					memo[''.join(c)] = 1
					dq.put(depth+1)
					if isleaf(c):
						return depth

T = int(raw_input())
for kk in xrange(T):
	s = raw_input()
	print "Case #%s:"%(kk+1), sBFS(s)

# k = 10
# for a in xrange(2**k):
# 	q = ("{0:0" + str(k) + "b}").format(a).replace('0','-').replace('1','+')
# 	print sBFS(q)

# print s
# print ''.join(m(list(s),7))
        

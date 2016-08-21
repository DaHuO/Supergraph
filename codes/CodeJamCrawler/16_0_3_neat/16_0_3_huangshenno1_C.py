import sys

N = 32
J = 500

def get_div(x):
#   for a in xrange(3, int(x**0.5)+1, 2):
    for a in xrange(3, min(int(x**0.5)+1, 1000000), 2):
	if x % a == 0:
	    return a
    return 0

def b_base(x, b):
    ret = 0
    for c in x:
	ret = ret * b + int(c)
    return ret

def check(x):
    div = []
    for b in xrange(2, 10+1):
	y = b_base(x, b)
	d = get_div(y)
	if d > 0:
	    div.append(d)
	else:
	    return False
    print x+' '+' '.join(map(str, div))
    return True

def find(a, b):
    ans = 0
    for i in xrange(a, b):
	x = bin(i)[2:] + '1'
	if check(x):
	    ans += 1
	    if ans == J: return

if __name__ == '__main__':
#   print 'Case #1:'
#   find(2**(N-2), 2**(N-1))
    if len(sys.argv) != 3:
	print 'Usage: python C.py a b'
	exit()
    a, b = map(int, sys.argv[1:3])
    find(a, b)

import collections as clt

table = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE','TEN']
tlen = [clt.Counter(s) for s in table]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def _remove(count, n):
    cnt = count.copy()
    cnt.subtract(clt.Counter(table[n]))
    if all([v >= 0 for v in cnt.itervalues()]):
        return cnt
    else:
        return None

def _recur(count, n, num):
    if n == 10:
        if all([v == 0 for v in count.itervalues()]):
            return num
        else:
            return None
    cp = count.copy()
    cp2 = num
    while True:
        nn = _recur(count, n + 1, num)
        if nn != None:
            return nn
        count = _remove(count, n)
        if count != None:
            num += str(n)
        else:
            break
    count = cp
    num = cp2
    return None

def solve(S):
    return _recur(clt.Counter(S), 0, '')

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange(t):
		S = raw_input()
		print "Case #{}: {}".format(i + 1, solve(S))


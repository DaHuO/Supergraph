def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()

l = []


def digits(M):
	digit = []
	while M!=0 :
		m = M % 10
		if m in l:
			l.remove(m)
		M = M / 10
	
def solve(N) :
	if N == 0 :
		return -1
	else :
		for i in range(0,10):
			l.append(i)
		i = 1
		M = N
		while len(l) != 0:
			K = i *M
			digits(K)
			i += 1
		return M * (i-1)		
			
for t in range(_T):
	N = readint()
	res = solve (N)
	if res == -1 :
		print 'Case #%i:'%(t+1), 'INSOMNIA'
	else:
		print 'Case #%i:'%(t+1), res
		

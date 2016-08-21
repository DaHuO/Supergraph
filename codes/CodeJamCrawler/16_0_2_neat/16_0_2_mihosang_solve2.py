def calc(N):
	pool = [ N[0] ]
	for i in range(1,len(N)):
		if N[i] == N[i-1]:
			continue
		else:
			pool.append(N[i])
	if pool[len(pool)-1] == '+':
		return len(pool)-1
	else:
		return len(pool)

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(1,T+1):
		N = raw_input()
		result = calc(N)
		print 'Case #%d: %d' % (i,result)

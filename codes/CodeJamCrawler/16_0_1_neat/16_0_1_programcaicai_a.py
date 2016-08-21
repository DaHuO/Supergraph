n = int(raw_input())
xs = [int(raw_input()) for _ in range(n)]


def solve(x):
	if x == 0:
		return 'INSOMNIA'
	else:
		vis = [0]*10
		nvis = 10
		now = 0
		while nvis != 0:
			now +=x
			tnow = now
			while tnow:
				if not vis[tnow%10]:
					vis[tnow%10]=1
					nvis-=1
				tnow/=10
			
		return now

for i,x in enumerate(xs):
	print 'Case #{}: {}'.format(i+1,solve(x))





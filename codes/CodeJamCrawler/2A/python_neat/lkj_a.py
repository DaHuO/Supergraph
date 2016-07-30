def getprs(n,w):
	c = w
	for i in range(n):
		nc = ''
		for l in c:
			nc += {'P':'PR', 'R':'SR', 'S':'SP'}[l]
		c = nc
	return [c.count(ch) for ch in 'PRS']

def getsol(n,w):
	c = w
	for i in range(n):
		nc = ''
		for l in c:
			nc += {'P':'PR', 'R':'SR', 'S':'SP'}[l]
		c = nc
	for loginvsize in range(0,n):
		#print('swapping loginvsize {}, starting with: {}'.format(loginvsize, c))
		for sgind in range(0,2**n,2**(loginvsize+1)):
			if c[sgind:sgind+2**loginvsize] > c[sgind+2**loginvsize:sgind+2*2**loginvsize]:
				c = c[:sgind] + c[sgind+2**loginvsize:sgind+2*2**loginvsize] + c[sgind:sgind+2**loginvsize] + c[sgind+2*2**loginvsize:]
	return c

def solve(n,r,p,s):
	pprs = getprs(n,'P')
	rprs = getprs(n,'R')
	sprs = getprs(n,'S')
	#print(pprs, rprs, sprs)
	if not [p,r,s] in [pprs, rprs, sprs]:
		return 'IMPOSSIBLE'
	else:
		return getsol(n,'PRS'[[pprs, rprs, sprs].index([p,r,s])])

tc = int(input())
for t in range(1,tc+1):
	n,r,p,s = [int(x) for x in input().split()]
	print('Case #{}: {}'.format(t,solve(n,r,p,s)))

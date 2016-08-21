import sys
lines = sys.stdin.readlines()
write = sys.stdout.write
def solve(n):
	cnt = 0
	pre = n[0]
	for i in range(len(n)):
		if n[i]!=pre:
			cnt+=1
			pre=n[i]
	cnt+=pre=='-'
	return cnt

t = int(lines[0])
for i in range(1,t+1):
	#print 'lines',lines[i],type(lines[i])
	n=lines[i].replace('\n','')
	res = solve(n)
	res = str(res)
	write('Case #%d: %s\n'%(i,res))
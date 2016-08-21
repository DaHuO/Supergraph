import sys
lines = sys.stdin.readlines()
write = sys.stdout.write
def solve(k,c,s):
	if k ==s:
		return ' '.join(map(str,range(1,s+1)))
	return 'IMPOSSIBLE'



t = int(lines[0])
for i in range(1,t+1):
	#print 'lines',lines[i],type(lines[i])
	K,C,S=map(int,lines[i].replace('\n','').split(' '))
	res = solve(K,C,S)
	res = str(res)
	write('Case #%d: %s\n'%(i,res))
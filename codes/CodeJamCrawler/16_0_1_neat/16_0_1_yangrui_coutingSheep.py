import sys
lines = sys.stdin.readlines()
write = sys.stdout.write
def solve(n):
	if n=='0':
		return 'INSOMNIA'
	seen=set()
	n = int(n)
	pre = n
	while len(seen)<10:
		tmpn =str(n)
		for i in range(len(tmpn)):
			seen.add(tmpn[i])
		#print seen
		n +=pre
		#print 'n',n
	return n-pre

t = int(lines[0])
for i in range(1,t+1):
	#print 'lines',lines[i],type(lines[i])
	n=lines[i].replace('\n','')
	res = solve(n)
	res = str(res)
	write('Case #%d: %s\n'%(i,res))
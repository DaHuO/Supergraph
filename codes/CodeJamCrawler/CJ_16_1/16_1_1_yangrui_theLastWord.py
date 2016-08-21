import sys
lines = sys.stdin.readlines()
write = sys.stdout.write
def solve(s):
	res = s[0]
	for i in range(1,len(s)):
		if s[i]<res[0]:
			res+=s[i]
		else:
			res = s[i]+res
	return res

t = int(lines[0])
for i in range(1,t+1):
	#print 'lines',lines[i],type(lines[i])
	s=lines[i].replace('\n','')
	res = solve(s)
	res = str(res)
	write('Case #%d: %s\n'%(i,res))
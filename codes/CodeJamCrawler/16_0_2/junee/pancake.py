f = open('test.txt','r')
a = open('ans.txt','w')
for i in range(1,int(f.readline())+1):
	s = f.readline()
	ans = 0
	if s[0] == '-':
		ans+=1
	state = s[0]
	for j in s[1:]:
		if state == j:
			continue
		elif state=='+' and j=='-':
			state=j
			ans+=2
		elif state=='-' and j=='+':
			state=j
	a.write('Case #%d: %d\n'%(i,ans))
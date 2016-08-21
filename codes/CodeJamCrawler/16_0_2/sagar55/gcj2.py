import sys

def solve(s):
	l = len(s)
	i = 0
	plain_start = -1
	if s[0] == '-':
		plain_start = 0 
	i = 1
	cnt = 0 
	while i<l:
		if s[i]=='+' and s[i-1]=='-':
			if(plain_start == 0):
				cnt+=1
			else:
				cnt+=2
			plain_start = -1
		elif s[i]=='-':
			if plain_start == -1:
				plain_start = i
		i+=1
	if plain_start==0:
		cnt+=1
	elif plain_start>0:
		cnt+=2
	return cnt

with open('in.txt') as f:
	sys.stdout = file('out.txt', 'w')
	t = int(f.readline())
	for nT in range(1,t+1):
		s = f.readline()
		print "Case #%d:"%nT,solve(s)


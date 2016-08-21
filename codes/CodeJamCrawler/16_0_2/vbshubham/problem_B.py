def strip(s):
	while(s and s[-1]):
		s.pop()
	return s 
def flip(s,i):
	part = [not l for l in s[:i]]
	part.reverse()
	s = part+s[i:]
	return s
t = int(raw_input())
cnt = 0
while cnt<t:
	cnt+=1
	S = raw_input()
	S = [True if l=='+' else False for l in S ]
	S = strip(S)
	res = 0
	while(S):
		if S[0]==False:
			S = flip(S,len(S))
		else:
			i=0
			while(S[i]):
				i+=1
			S = flip(S,i)
		# print S
		res+=1
		S = strip(S)
	print 'Case #%d:'%cnt,res

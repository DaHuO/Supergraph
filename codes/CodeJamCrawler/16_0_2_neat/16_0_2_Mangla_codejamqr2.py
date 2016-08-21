fo = open("foo1.txt", "wb")
def reverse(s):
	rs = s[::-1]
	rs = list(rs)
	for i in range(len(rs)):
		if rs[i]=='+':
			rs[i]='-'
		elif rs[i] == '-':
			rs[i]='+'
	return ''.join(rs)	
t = input()
f = 1
while t:
	s = raw_input()
	ans = 0
	while(len(s)!=0):
		rs = s[::-1]
		i = rs.find('-')
		if i == -1:
			break
		rs = rs[i:]
		s = rs[::-1]
		j = s.find('-')
		if(j > 0):
			w = s[:j]
			l = list(w)
			for i in range(len(l)):
				l[i] = '-'
			s = ''.join(l)+s[j:]
			ans +=1
		s = reverse(s)
		ans += 1
	print ans
	fo.write('Case #'+str(f) + ': '+str(ans)+'\n');
	t = t -1
	f += 1
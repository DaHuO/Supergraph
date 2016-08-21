co = 0
#Swap + >> - : +++-- >> ---+++
def dec(s):
	f = 0
	if s[0]=='+' and s[-1]=='-':
		i = 0
		f = 1
		while s[i] == '+':
			s[i] = '-'
			i+=1
	return s,f
#Cambiar todos ---+- >> +-++++
def ret(s):
	f = 0
	if s[0]=='-' and s[-1]=='-':
		i=0
		f = 1
		while i<len(s):
			if s[i] == '+': s[i] = '-'
			else: s[i] = '+'
			i+=1
	return s[::-1], f
def eli(p):
	for x in reversed(range(len(p))):
		if p[x] == '-': break
		else: p = p[:-1]
	return p
t = int(raw_input())
for y in range(t):
	p = raw_input()
	p = [x for x in p]
	i=0
	while '-' in p:
		p = eli(p)
		p,f1 = dec(p)
		p,f2 = ret(p)
		i += f1+f2
	print "Case #%s: %s" % (str(y+1), str(i))


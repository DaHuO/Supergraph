input_file = open('B-large.in', 'r+')
output_file = open('B-large.out', 'w+')
t = int(input_file.readline())
c = 0
while(c<t):
	c += 1
	s = input_file.readline().strip()
	#print line
	o = 0
	if(s[-1]=='-'):
		o += 1
	l = len(s)-2
	while(l>=0):
		if(s[l]=='+' and s[l+1]=='-'):
			o += 1
		elif(s[l]=='-' and s[l+1]=='+'):
			o += 1
		l -= 1
	output_file.write('Case #'+str(c)+': '+str(o)+'\n')

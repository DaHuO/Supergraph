f = open('A-large.in','r')
out = open('outputLarge.txt','w')
def generateLastWord(s):
	if s in "": return s
	tmp = s[0]
	for i in s[1:]:
		if tmp[0] <= i:
			tmp = i+tmp
		else:
			tmp = tmp+i
	return tmp


tests = f.readline()
for i in range(1,int(tests)+1):
	s =  f.readline().strip()
	ans = generateLastWord(s)
	out.write("Case #"+str(i)+ ": "+str(ans)+"\n")
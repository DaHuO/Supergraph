t=input()
char=list()
temp=str()
case=1
while t is not 0:
	s=raw_input()
	char=[str(0)]
	char[0]=s[0]
	i=0
	for i in xrange(1,len(s)):
	    if ord(char[0])>ord(s[i]):
	        char.append(s[i])
	        ##print char
	    else:
	        char.insert(0,s[i])
	        ##print char
	for i in xrange(len(char)):
	    temp+=char[i]
	    
	print "Case #"+str(case)+": "+temp
	temp=""
	case+=1
	
	t-=1

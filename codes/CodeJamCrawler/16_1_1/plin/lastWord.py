a=open('word-in-large.txt','r')
b=a.readlines()
for i in range(len(b)):
	b[i]=b[i].rstrip('\n')
a.close()

c=open('word-out-large.txt','w')

def addLetter(curWord,letter):
	if (ord(letter)>=ord(curWord[0])):
	    return (letter+curWord)
	return (curWord+letter)
		
for i in range(1,len(b)):
	temp=b[i]
	result=temp[0]
	for j in range(1,len(temp)):
	    result=addLetter(result,temp[j])
	tempStr="Case #"+str(i)+": "+result+"\n"
	c.write(tempStr)

c.close()
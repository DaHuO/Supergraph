a=open('pancake-in-large.txt','r')
b=a.readlines()
for i in range(len(b)):
	b[i]=b[i].rstrip('\n')
a.close()

c=open('pancake-out-large.txt','w')

def flipStack(temp,i):
	for i in range(i):
		if temp[i]=="+":
			temp[i]="-"
		else:
			temp[i]="+"

for i in range(1,len(b)):
	result="Case #"+str(i)+": "
	stack=b[i]
	stackList=list(stack)
	flipNum=0
	for i in range(len(stackList)-1,-1,-1):
		if stackList[i]=="-":
			flipStack(stackList,i+1)
			flipNum+=1
	result+=str(flipNum)+"\n"
	c.write(result)
c.close()
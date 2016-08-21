import time
def checker(s):
	for i in s:
		if i!='+':
			return 0
	return 1
def rev(s):
	l=[]
	S=""
	for i in s:
		l.append(i)
	for i in l:
		if i=='+':
			S+='-'
		else:
			S+='+'
	return S
f=open('output','w')
case=1
for t in range(int(input())):
	s=input()
	count=0
	l=len(s)
	while(True):
		m=False
		start=-1
		started=-1
		for i in  range(l-1,-1,-1):
			if s[i]=='-':
				m=True
				start=i
				for j in range(i-1,-1,-1):
					if s[j]=='-':
						started=j
					else:
						break
			if start!=-1:
				break
		to=-1
		if m==True:
			if s[0]=='+':
				to=0
				for j in range(1,start):
					if s[j]=='+':
						to=j
					else:
						break
		if to>-1:
			t=rev(s[:to+1])
			s=t[::-1]+s[to+1:]
			count+=1
		if m==True:
			t=s[:start+1]	#start->started
			t=rev(t)[::-1]	#start->started
			s=t+s[start+1:]
			count+=1
		c=checker(s)
		if c==1:
			f.write("Case #"+str(case)+":"+" "+str(count)+"\n")
			case+=1
			break
f.close()
			
			

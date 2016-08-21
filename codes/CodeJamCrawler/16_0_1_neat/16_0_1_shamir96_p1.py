def func(s):
	if(s=='0'):
		return "INSOMNIA"
	else:
		s1=s
		next=1
		j=[0]*10
		while(not(all(j))):
			for i in s:
				j[int(i)]=1
			next=next+1
			s=str(next*int(s1))
		return int(s)-int(s1)
	
t=input()
s=[]
for i in range(int(t)):
	s.append(input())
for i in range(int(t)):
	text="Case #"+str(i+1)+":"
	print(text,func(s[i]))	

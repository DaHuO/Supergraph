def find(a):
	q1=set(map(int,a))
	L=pow(10,len(a)+1)
	a=int(a)
	b=a

	for i in range(1,L):
		q2=set(map(int,str(a)))
		#print(q2)
		q1=q1|q2
		#print(q1)
		if len(q1) == 10:
			return a;
		a=a+b;
	return 'INSOMNIA'


t=int(input())

for i in range(1,t+1):
	a=input()
	v=find(a)
	s="Case #"+str(i)+":"
	print(s,v);
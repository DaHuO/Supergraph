def f(s):
	bit=[]
	count=0
	for i in s:
		if i=="+":
			bit.append(1)
		else:
			bit.append(0)
	while not(all(bit)):
		count=count+1
		start=bit[0]
		j=0
		#for i in range(len(bit))
		while(j<len(bit) and bit[j]==start):
			bit[j]=not(bit[j])
			j=j+1
	return count
t=input()
s=[]
for i in range(int(t)):
	s.append(input())
for i in range(int(t)):
	text="Case #"+str(i+1)+":"
	print(text,f(s[i]))	

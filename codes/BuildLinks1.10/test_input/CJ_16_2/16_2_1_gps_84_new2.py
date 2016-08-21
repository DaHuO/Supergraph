def mark(l1,a):
	for i in range(len(l1)):
		if l1[i]==a:
			l1[i]='a'
			return


t=int(input())
abc=0
while abc!=t:
	abc+=1
	count=[0,0,0,0,0,0,0,0,0,0]
	s=input()
	l1=[]
	for i in s:
		l1.append(i)

	while 'Z' in l1:
		mark(l1,'E')
		mark(l1,'R')
		mark(l1,'O')
		mark(l1,'Z')
		count[0]+=1
	while 'X' in l1:
		mark(l1,'I')
		mark(l1,'S')
		mark(l1,'X')
		count[6]+=1
	while 'U' in l1:
		mark(l1,'F')
		mark(l1,'O')
		mark(l1,'U')
		mark(l1,'R')
		count[4]+=1
	while 'F' in l1:
		mark(l1,'F')
		mark(l1,'I')
		mark(l1,'V')
		mark(l1,'E')
		count[5]+=1
	while 'V' in l1:
		mark(l1,'S')
		mark(l1,'E')
		mark(l1,'V')
		mark(l1,'E')
		mark(l1,'N')
		count[7]+=1
	while 'G' in l1:
		mark(l1,'E')
		mark(l1,'I')
		mark(l1,'G')
		mark(l1,'H')
		mark(l1,'T')
		count[8]+=1
	while 'I' in l1:
		mark(l1,'N')
		mark(l1,'I')
		mark(l1,'N')
		mark(l1,'E')
		count[9]+=1
	while 'H' in l1:
		mark(l1,'T')
		mark(l1,'H')
		mark(l1,'R')
		mark(l1,'E')
		mark(l1,'E')
		count[3]+=1
	while 'W' in l1:
		mark(l1,'T')
		mark(l1,'W')
		mark(l1,'O')
		count[2]+=1
	while 'N' in l1:
		mark(l1,'O')
		mark(l1,'N')
		mark(l1,'E')
		count[1]+=1
	print("Case #",abc,": ",sep='',end='')
	for i in range(0,10):
		print(str(i)*count[i],end='')
	
	print()
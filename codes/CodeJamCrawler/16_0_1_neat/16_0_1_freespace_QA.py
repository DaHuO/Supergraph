C = int(input())

for case in range(C):
	N = input()
	ans = [0 for x in range(11)]
	c = 0
	m = 2
	temp=N
	if(temp!='0'):
		for t in temp:
			ans[int(t)]=1
		
		while(sum(ans)!=10):
			temp=str(int(N)*m)
			m+=1
			for t in temp:
				ans[int(t)]=1
		
	else: temp='INSOMNIA'
	print("Case #%d:"%(case+1),temp)
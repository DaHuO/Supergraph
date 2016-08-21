t=int(input())
for i in range(t):
	pan=input()
	a=pan.count('+-')+pan.count('-+')
	if(pan[len(pan)-1]=='-'):
		a+=1	
	print("Case #"+str(i+1)+": "+str(a))	









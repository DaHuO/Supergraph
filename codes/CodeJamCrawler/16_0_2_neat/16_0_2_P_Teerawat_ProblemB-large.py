def IsAllHappy( List ):
	for i in range(len(List)):
		if List[i]=='-':
			return 0
	return 1
	
def FliptoHappy( List ):
	i = len(List)
	while i>0:
		if List[i-1]=='+':
			i=i-1
		else:
			break
	while i>0:
		if List[i-1]=='+':
			List[i-1]='-'
		else:
			List[i-1]='+'
		i=i-1
	return List

Input=open('B-large.in','r')
Output=open('output-large.out','w')

T = int(Input.readline())
if T < 0 or T > 100:
	print "T is out of range"
else:
	for i in range(T):
		S = list(Input.readline())
		if '\n' in S:
			S.remove('\n')
		y=0
		while IsAllHappy(S)!=1:
			S = FliptoHappy(S)
			y=y+1
		Output.write("Case #"+str(i+1)+": "+str(y)+"\n")
		
Input.close()
Output.close()
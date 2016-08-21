def findPos(a,s):
	for i in range(len(a)):
		if a[i]==s:
			return i;
	return len(a)		
def check(a):

	for i in a:
		if i == '-':
			return False;
	return True;		

def find(a):
	pos=0;
	count=0
	while check(a) is not True:
		if a[0] == '+':
			pos=findPos(a,'-')
			a=('-'*pos)+a[pos:]	
		else:
			pos=findPos(a,'+')
			a=('+'*pos)+a[pos:]
		
		count=count+1		
	return count	





t=int(input())

for i in range(1,t+1):
	a=input()
	v=find(a)
	s="Case #"+str(i)+":"
	print(s,v);
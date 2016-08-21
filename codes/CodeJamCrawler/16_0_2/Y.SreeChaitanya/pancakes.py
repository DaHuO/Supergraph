f=open("b.in","r")
count=0
mincount=999
t=int(f.readline().rstrip("\n"))
def flip(i,string):
	copy=""
	global count
	for k in range(0,i):
		if(string[k]=='+'):
			copy+='-'
		else:
			copy+='+'
	copy+=string[i:]
	count+=1
	##print(copy)
	return copy



def evaluate(s):
	for x in s:
		if(x == '-'):
			return False
	return True
for i in range(0,t):
	string=f.readline().rstrip("\n")
	count=0
	while(evaluate(string)==False):
		##print(string)
		fc=string[0];
		j=1;
		while(j<len(string) and string[j]==fc ):
			j=j+1;
		if(fc=='+' and len(string)!=1):
			k=0
			while(k<len(string) and string[k]=='-'):
				j=j+k
		if(fc=='-' and len(string)!=1):
			k=0
			if('-' in string[j:]):
				while(k<len(string) and string[k]=='+'):
					j=j+k
					
		string=flip(j,string)
	print("Case #"+str(i+1)+": "+str(count))




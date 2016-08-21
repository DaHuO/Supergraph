array=[]
f=open("a.in","r")

def mark(i,j):
	global array
	if('1' in str(i*j)):
		array.append('1') 
	
	if('2' in str(i*j)):
		array.append('2')
	
	if('3' in str(i*j)):
		array.append('3')
	
	if('4' in str(i*j)):
		array.append('4')
	
	if('5' in str(i*j)):
		array.append('5')
	
	if('6' in str(i*j)):
		array.append('6')
	
	if('7' in str(i*j)):
		array.append('7')
	
	if('8' in str(i*j)):
		array.append('8')
	
	if('9' in str(i*j)):
		array.append('9')
	
	if('0' in str(i*j)):
		array.append('0')
def evaluate():
	count=0;
	for i in range(0,10):
		if(str(i) in array):
			count=count+1;
	if(count==10):
		return True;

t=int(f.readline().rstrip("\n"))
for i in range (0,t):
	##global array
	n=int(f.readline().rstrip("\n"))
	array=[]
	for j in range (1,74):
		mark(n,j)
		if(evaluate()):
			print("Case #"+str(i+1)+": "+str(n*j))
			break;
		if(j==73):
			print("Case #"+str(i+1)+": "+"INSOMNIA");



G = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def multiples(n):
	if(n==0):
		return ("INSOMNIA")
	m = []
	for i in range(1,200):
		a = i*n
		#print(a)
		l = list(set([int(i) for i in str(a)]))
		m = m + l
		x = list(set(m))
		#print(x)
		if(x==G):
			return(a)
			break;
x = int(input())
for i in range(0,x):
	a = int(input())
	print("Case #",i+1,": ",multiples(a), sep='')
	

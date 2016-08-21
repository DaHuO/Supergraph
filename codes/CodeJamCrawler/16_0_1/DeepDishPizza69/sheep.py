

def process(n):

	if n==0:
		return "INSOMNIA"

	m=n	
	a=set()
	i=int(1)
	while (True):
		for x in str(m):
			a.add(x)
		
		#print str(n)+ "  ->>>  set(A) is "+str(a)
		if len(a)==10:
			break

		i=i+1
		#print "i is "+str(i)
		m=i*n


	#print "Last number is "+str(m)
	return m


def main():
	index=0
	with open("A-large.in", "r") as ins:
		numOfTestCases=int(ins.readline())
		#print "#cases "+str(numOfTestCases)
		

		cases=[]
		for i in range(numOfTestCases):
			n=int(ins.readline())
			
			lastNumber=process(n)
			# Case #1: 2 3
			print "Case #"+str(i+1)+": "+str(lastNumber)
			#break



main()
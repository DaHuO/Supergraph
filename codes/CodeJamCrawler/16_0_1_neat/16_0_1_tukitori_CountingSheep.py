fin = open('A-large.in','r')
fout = open('large.out','w+')
		
def print_case(caseNum,time):
	fout.write('Case #%d: %d\n' % (caseNum+1,time))

totalCases = int(fin.readline())
for i in range(totalCases):
	n = int(fin.readline())
	if (n==0):
		fout.write('Case #%d: INSOMNIA\n' % (i+1))
	else:
		a = [0,1,2,3,4,5,6,7,8,9]
		b = [True,True,True,True,True,True,True,True,True,True]
		j=1
		while True:
			current = n*j
			while current:
				digit = current % 10
				if (b[digit]):
					a.remove(digit)
					b[digit]=False
				if (len(a)==0):
					break;
				current //= 10
			if (len(a)==0):
				break;
			j+=1
		print_case(i,n*j)
		
	
fout.close()
fin.close()
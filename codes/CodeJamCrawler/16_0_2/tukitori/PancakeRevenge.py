fin = open('B-large.in','r')
fout = open('large.out','w+')
		
def print_case(caseNum,time):
	fout.write('Case #%d: %d\n' % (caseNum+1,time))

totalCases = int(fin.readline())
for i in range(totalCases):
	s = fin.readline()
	current = s[0]
	time = 0
	for c in s:
		if (c=='-' or c=='+'):
			if (current!=c):
				time+=1
			current=c
	if (current=='-'):
		time+=1
	print_case(i,time)
	
fout.close()
fin.close()
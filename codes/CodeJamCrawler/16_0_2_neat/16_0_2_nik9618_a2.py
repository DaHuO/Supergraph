f = open('/Users/nik9618/Downloads/B-large.in', 'r')
case = 0
f.readline()
for line in f.readlines():
	line = line.split("\n")[0]
	case +=1
	countchg = 0
	current = line[0] 
	for i in line: 
		if(i!=current):
			countchg+=1
			current = i
		else:
			continue;

	if(line[-1]=='-'):
		countchg+=1
	print "Case #"+str(case)+": "+str(countchg)


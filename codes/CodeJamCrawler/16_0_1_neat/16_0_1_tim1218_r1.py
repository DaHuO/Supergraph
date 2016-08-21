#exec(open('C:/Users/Taili/Desktop/r1.py').read())

def r1_run(num):
	n = num
	bucket = {}
	cout = 1
	while(cout<200):
		for singlenum in n:
			if singlenum not in bucket:
				bucket[singlenum] = 1
				if len(bucket) == 10:
					return n
		cout +=1
		n = str(long(num)*cout)
	return "not found"


f = open('C:/Users/Taili/Desktop/A-large.in', 'r')
outputfile = open('C:/Users/Taili/Desktop/A-large.out', 'w')
count = 0
for line in f:
	if count == 0: 
		count += 1 
		continue
	line = line.split('\n')
	if line[0] == '0':
		s = "Case #%d: INSOMNIA" %(count)
		print s 
		outputfile.write(s+'\n')
	else:
		#print "Case #%d: %s test num is %s" % (count , r1_run(line[0]), line[0])
		s = "Case #%d: %s" % (count , r1_run(line[0]))
		print s
		outputfile.write(s+'\n')
	count += 1
f.close()
outputfile.close()	

	




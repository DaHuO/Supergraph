r = open("A-large.in", 'r')
r2 = open("A-large.out",'w')
caseNumber = 1
r.readline()

for line in r.readlines():
	n = int(line[0:-1])
	r2.writelines("Case #" + str(caseNumber)+": ")
	bools = [0]*10

	for k in range(1, 10000):
		for q in [int(i) for i in list(str(n*k))]:
			bools[q] = 1
		if bools.count(0) == 0:
			r2.writelines(str(k*n)+'\n')
			break

	if bools.count(0) != 0:aa-l
		r2.writelines("INSOMNIA\n")
	caseNumber += 1
	
r.close()
r2.close()
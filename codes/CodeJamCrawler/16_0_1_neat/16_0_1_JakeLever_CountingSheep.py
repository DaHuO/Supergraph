import fileinput

def countSheep(N):
	if N == 0:
		return "INSOMNIA"

	count = 0
	awake = True
	used = [ False for _ in range(10) ]
	while awake:
		count += 1
		Nstr = str(count*N)

		used = [used[i] or (str(i) in Nstr) for i in range(10) ]
		awake = not all(used)

	return str(count * N)

#print countSheep(1692)

#for i in range(100000):
#	print i, countSheep(i)

caseCount = None
for i,line in enumerate(fileinput.input()):
	lineInt = int(line.strip())
	if caseCount is None:
		caseCount = lineInt
	else:
		print "Case #%d: %s" % (i,countSheep(lineInt))


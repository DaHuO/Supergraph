t = int(raw_input())
for i in xrange(1, t + 1):
	line = list(raw_input())
	lineLen = len(line)
	#print "input = ",line
	numFlips = 0
	line.reverse();
	try:
		index = line.index("-")
		index = lineLen-index-1;
		line.reverse();
	except ValueError:
		index = -1
	while index != -1:
				numFlips += 1
				for j in xrange(0,index+1):
					line[j] = "-" if line[j]=="+" else "+"
				#print "flipped = ",line
				try:
					line.reverse();
					index = line.index("-")
					index = lineLen-index-1;
					line.reverse();
				except ValueError:
					index = -1
				#print index
	print "Case #{}: {}".format(i, numFlips)

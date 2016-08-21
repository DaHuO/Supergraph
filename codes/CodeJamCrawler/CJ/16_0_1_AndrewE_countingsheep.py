#first line is number of cases
#proceeding will produce output
lines = [line.rstrip('\n') for line in open("large")]
master = set(['0','1','2','3','4','5','6','7','8','9'])
case = -1

#grab from list
for l in lines:
	case+=1
	n = 1
	#check if it can be done
	if (int(l)*2) == (int(l)):
		print "Case #" + str(case) + ": INSOMNIA"
	else:
		if master.issubset(l):
			print "Already has every number"
		bigl = l
		while master.issubset(bigl) == False:
			n+=1
			bigl += str(int(l)*n)
			#print bigl
			if(master.issubset(bigl)):
				print "Case #" + str(case) + ": " + str(n*int(l))
def isContainAll(contain):
	return ("0" in contain) and ("1" in contain) and ("2" in contain) and ("3" in contain) and ("4" in contain) and ("5" in contain) and ("6" in contain) and ("7" in contain) and ("8" in contain) and ("9" in contain)

#print isContainAll("0123456789")	

case = raw_input()

for i in xrange(1,int(case)+1):
	start = raw_input()
	start = int(start)
	
	if start == 0:
		print "Case #"+str(i)+": INSOMNIA"
	else:
		contain = ""
		j = 1
		counting = start
		while not isContainAll(contain):
			contain += str(counting)
			j += 1
			lastcounting = counting
			counting = j*start
			
		print "Case #"+str(i)+": "+str(lastcounting)
			
	#print i
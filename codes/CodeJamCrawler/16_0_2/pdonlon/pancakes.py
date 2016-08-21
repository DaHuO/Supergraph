cases = int(raw_input())

for c in range(0,cases):
	
	panstack = raw_input()
	
	started = False
	counter = 0
	panstack += "+" 
		
	for i in range(len(panstack)-2,-1,-1):
		if panstack[i] != panstack [i+1]:
			counter += 1
	print "Case #"+str(c+1)+": "+str(counter)
		
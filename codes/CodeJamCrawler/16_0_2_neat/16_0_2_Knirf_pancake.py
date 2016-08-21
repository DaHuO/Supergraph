def getResult(n):
	changed=0
	if(n[0]=='-'):
		changed=1
	current = '+'
	plusIndex = n.find('+')
	if(plusIndex!=-1):
		for c  in n[plusIndex:]:
			if(current == c):
				pass
			else:
				current = c
				if(c == '-' ):
					changed+=2
	return changed	

t = int(raw_input()) 
for i in xrange(1, t + 1):
  n = raw_input() 
  result = getResult(n)
  print "Case #{}: {}".format(i, result)
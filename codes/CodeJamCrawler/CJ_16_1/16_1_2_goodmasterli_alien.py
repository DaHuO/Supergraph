from sets import Set 
filein = open('B-large.in', 'r')
fileout = open('B-large.out', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    TT = int(filein.readline())
    inp = []
    for tt in range(TT*2-1):
    	inp.append([int(x) for x in filein.readline().split()])
    
    result = []

    for i in range(TT):
    	seen = []
    	for j in range(TT*2-1):
    		seen.append(inp[j][i])
    	val = sorted(seen)[2*i]
    	# print seen
    	# print val

    	candidates = []
    	for j in range(TT*2-1):
    		if inp[j][i] == val:
    			candidates.append(inp[j])
    	if len(candidates) == 1:
    		seen.append(val)
    		# print candidates
    		# print seen
    		for x in candidates[0]:
    			seen.remove(x)
    		result = sorted(seen)
    for u in result:
    	fileout.write(str(u)+" ")
    fileout.write("\n")		

    
 
filein.close()
fileout.close()
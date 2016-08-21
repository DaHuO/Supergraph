import fileinput

i = 0
for line in fileinput.input():
    line = line.strip()
    if i == 0:
        testcases = int(line)
    else:
    	n = int(line)
    	nnext = n
    	if n == 0:
    		print("Case #%d: INSOMNIA" % i)
    	else:
    		a_set = set()
    		multiplier = 2
    		while len(a_set) < 10:
    			digits = map(int,str(nnext))
    			a_set |= set(digits)
    			old = nnext
    			nnext = n*multiplier
    			multiplier += 1
    		print("Case #%d: %d" % (i, old))
    i += 1
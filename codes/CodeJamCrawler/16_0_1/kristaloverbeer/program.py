test_cases = int(input())
for t in range(test_cases):
    
    number = int(input())

    if number == 0:
    	print("Case #%d: INSOMNIA" % (t+1))
    else:
	    res = set()

	    i = 0
	    while len(res) < 10:
	        i += 1
	        cpt = number * i
	        res = res | set([x for x in str(cpt)])

	    print("Case #%d: %d" % (t+1, cpt))
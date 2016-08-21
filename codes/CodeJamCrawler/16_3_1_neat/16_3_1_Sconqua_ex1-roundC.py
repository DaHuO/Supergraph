import operator
# Number of test cases
n = int(raw_input())
#print "NUMERO CASI %d " % n

for test in xrange(1, n+1):
	npartiti = int(raw_input())
#	print "%d partiti" % npartiti
	nsenatori = [int(i) for i in raw_input().split(" ")]
#	print "numero senatori: "
#	print nsenatori
	

	if npartiti == 2:
		if (sum(nsenatori) / nsenatori[0]) == 2:
			result = ''.join("AB " for j in range(1, nsenatori[0]+1))
			print "Case #{}: {}".format(test, result[:-1])
			continue


	lettera = "A"

	result = list()
	counter = 0

	for sen in nsenatori:
		result.append([lettera, sen])
		lettera = chr(ord(lettera) + 1) 

	#print result
	result.sort(key=operator.itemgetter(1), reverse=True)
	#print "ordine"
	#print result
	#print "somma %d" % sum(val for lett, val in result)

	somma = sum(val for lett, val in result)
	
	print "Case #{}:".format(test),
	while somma != 2:	
		result[0][1] -= 1
		print "{}".format(result[0][0]),
		result.sort(key=operator.itemgetter(1), reverse=True)
		somma = sum(val for lett, val in result)
	print "{}".format(result[0][0] + result[1][0])

#	print "Case #{}: {}".format(test, ''.join(str(x) for x in sorted(result, key=int)))
from itertools import combinations

raw_input() #dummy
N, J = map(int, raw_input().split())


#N = 32
#J = 500


indices = list(range((N/2)-1))

count = 1

print "Case #1:"
for i in range(0,len(indices)):
	for comb in combinations(indices, i+1):
		#print list(comb)
		string = list("1" + "0"*((N-1)/2))
		for index in list(comb):
			string[1+index] = "1"
		stringed = "".join(string)
		second = "0"*(len(stringed) - len(stringed.rstrip('0'))) + stringed.rstrip('0')
		#print "First part:", stringed
		#print "Second part:", second

		#for base in range(2,11):
		#	print "\t", int(stringed + second, base), "divisor=", int(second, base), "result:", float(int(stringed + second, base)) % float(int(second, base))

		print stringed+second, " ".join([str(int(second, base)) for base in range(2,11)])
		count += 1
		if count > J:
			exit()
def checkPrime(number):
	for z in range(2,100):
		if (number%z==0):
			return z
	return 0

#Taking input from file
inputfile = open("inputC.txt", "r")
testcases = long((inputfile.readline())[:1])
inputnumbers = inputfile.readline().split()
n = long(inputnumbers[0])
j = long(inputnumbers[1])

value = []
for l in range(0,9):
	value.append(long(0))

i = 0
k = 0

print "Case #1:"
while(1):
	#Generate a string
	binaryRep = bin(long(i))[2:]
	string = '1'
	for l in range(0,n-2-len(binaryRep)):
		string += '0'
	string += binaryRep + '1'
	
	for l in range(0,9):
		value[l] = 0

	#Compute all value in different bases
	for l in range(0,n-1):
		for m in range(0,9):
			value[m] = (value[m] + long(string[l]))*(m+2)
		
	for m in range(0,9):
		value[m] += long(string[n-1])

	flag = 0
	output = []
	for m in range(0,9):
		temp = checkPrime(value[m])
		if(temp==0):
			flag = 1
			break
		output.append(temp)

	if (flag==1):
		i += 1
		continue

	outstr = string
	for m in range(0,9):
		outstr += " "+str(output[m])

	print outstr
	k += 1
	if (k==j):
		break

	i += 1
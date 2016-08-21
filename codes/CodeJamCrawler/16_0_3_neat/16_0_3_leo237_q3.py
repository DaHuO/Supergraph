import math

def produceDifferentNumber(lenN, previous):
	res = bin(int(str(previous),2)+2)[2:]
	if len(res)==lenN:
		return res
	else:
		return -1


def returnInt(number, base):
	return int(str(number),base)
	
def first_factor(n):
	n = int(n)
	print n
	lim = int(math.sqrt(n))+1
	for num in xrange(2, lim):
		if n % num == 0:
			return num
	print "PRIME"
	return -1
	

t = input()
t1 = t
final = ""
while t:
	n, j = map(int,raw_input().split(" "))
	found = 0
	numberToCheck="1"
	for i in xrange(n-2):
		numberToCheck+="0"
	numberToCheck += "1"
	finalResult = []
	while(found<j and numberToCheck != -1):
		print "checking ", numberToCheck
		solFactors = []
		for base in xrange(2,11):
			intToCheck = returnInt(numberToCheck,base)
			fac = first_factor(intToCheck)
			if (fac != -1):
				solFactors.append(fac)
			else:
				break
		if len(solFactors)==9:
			print "FOUND!!!!"
			found+=1
			solFactors.insert(0,numberToCheck)
			finalResult.append(solFactors)
		numberToCheck = produceDifferentNumber(n,numberToCheck)
				
	final+="Case #{0}:\n".format(t1-t+1)
	for each in finalResult:
		final += ' '.join(map(str,each))
		final +='\n' 
	t-=1
print final
output_file = open('q3_small.out','w')
output_file.write("{}".format(final))
output_file.close()


			
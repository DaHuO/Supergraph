import sys

if (len(sys.argv) < 2):
	print "Need inputfile as argument"
	exit(1)

#read file
input = list()
with open(sys.argv[1], 'r') as f:
	input = f.read().splitlines()
input.pop(0)

#convert to int list
input = map(lambda s: map(int, s.split(' ')), input)

def listToStr(indexList):
	indexListStr = ""
	for index in indexList:
		indexListStr += str(index)+" "
	indexListStr = indexListStr[:-1]
	return indexListStr

#compute
output = list()
for (k,c,s) in input:
	# if c = 1, gold couldn't have propagated, so we need to check every tile
	if (c == 1):
		if (s >= k):
			output.append(listToStr(range(1,k+1)))
		else:
			output.append("IMPOSSIBLE")
	else:
		# compute the minimal list of lookups needed
		indexList = list()
		if (k == 1):
			indexList.append(1)
		elif (k == 2):
			indexList.append(2)
		elif (k == 3):
			indexList.append(2)
			indexList.append(3)
		else:
			indexList = range(2,k-1)
			indexList.append(k**c -1)

		#see if minimal list of lookups is within the given limit
		if (len(indexList) > s):
			output.append("IMPOSSIBLE")
		else:
			output.append(listToStr(indexList))


#write file
with open('output_fractal.txt', 'w') as f:
	for (line, index) in zip(output, range(1,len(output)+1)):
		f.write("Case #"+str(index)+": "+str(line)+"\n")

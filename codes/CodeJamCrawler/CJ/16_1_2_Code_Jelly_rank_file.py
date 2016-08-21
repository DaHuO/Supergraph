import cProfile, pstats, io, getopt, sys
from collections import Counter

def findMissing(givenVals):
	output = []
	for key in Counter(givenVals).keys():
		if Counter(givenVals)[key] % 2 != 0:
			output.append(int(key))
	output.sort()
	newOut = [str(i) for i in output]
	outStr = " ".join(newOut)
	return outStr

def mainLogic(numCases, inFile):
	output=""
	for case in range(numCases):
		givenVals = []
		numLines = int(inFile.readline().strip())
		for i in range(numLines*2-1):
			for s in inFile.readline().strip().split(' '):
				givenVals.append(s)
		result = findMissing(givenVals)
		output = output+"Case #{}: {}\n".format(case+1,result)
	return output

inPath=""
try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:")
except getopt.GetoptError:
	print('Use -i to specify an input file')
	sys.exit(1)
for opt, arg in opts:
	if opt == '-h':
		print('Use -i to specify an input file')
		sys.exit()
	elif opt == '-i':
		inPath = arg
if inPath=="":
	inPath='test.in'
pr = cProfile.Profile()
pr.enable()
inFile = open(inPath,'rU')
outFile = open(inPath.replace('.in','')+'.out','w')
numCases = int(inFile.readline())
output = mainLogic(numCases, inFile)
outFile.write(output)
inFile.close()
outFile.close()
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

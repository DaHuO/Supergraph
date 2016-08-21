import time

def addHeightsToDict(x, dictHeights):
	if x in dictHeights:
		dictHeights[x] = dictHeights[x] + 1
	else:
		dictHeights[x]=1
	return dictHeights

start_time = time.time()

# f = open("B-small-attempt01.in")
# f = open("B-large01.in")
f = open("B-large1.in")
result = open('B-large1.in.txt', 'w')
# result = open('B-large-output.txt', 'w')

cases = int(f.readline().rstrip())
for x in xrange(0, cases):
	N = int(f.readline().rstrip())

	dictHeights = {}

	for h in xrange(0, 2*N - 1):
		rowCol = f.readline().rstrip().split()
		abc = map(lambda x: addHeightsToDict(x, dictHeights), rowCol)

	# get only odd (missing) items
	missingRowColDict = {k:v for k,v in dictHeights.iteritems() if v%2 != 0 }

	# convert missing row into sorted list
	missingRowCol = map(int, missingRowColDict.keys())
	missingRowCol.sort()

	print missingRowCol
	caseResult = "Case #"+str(x+1)+": " + ' '.join(map(str, missingRowCol)) + "\n"
	result.write(caseResult)
f.close()
result.close()

print("--- %s seconds ---" % (time.time() - start_time))


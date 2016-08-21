import sys
import time

def run(f):
	filename = sys.argv[1]

	iFile = open("input/%s.in" % (filename), "r")
	oFile = open("output/%s.out" % (filename), "w")

	numberOfCases = int(iFile.readline())
	startTime = time.clock()

	for case in range(numberOfCases):
		print("Case #%d started." % (case + 1))
		oFile.write("Case #%d: %s\n" % (case + 1, f(iFile)))
		print("Case #%d finished.\n" % (case + 1))

	endTime = time.clock()

	print("Runtime: %.2f seconds." % (endTime - startTime))

	iFile.close()
	oFile.close()
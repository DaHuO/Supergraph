import os

def findSpotsToCheck(numInitialTiles, complexityLevel, numStudents):
	spotsToCheck = []
	totalNumTiles = numInitialTiles ** complexityLevel
	finalTilesPerInitialTile = totalNumTiles / numInitialTiles
	if finalTilesPerInitialTile == 1:
		finalTilesPerInitialTile = 0
	for i in xrange(0, numInitialTiles):
		spotsToCheck.append(str((i + (finalTilesPerInitialTile*i)+1)))
	if len(spotsToCheck) > numStudents:
		return "IMPOSSIBLE"
	else:	
		return ' '.join(spotsToCheck)
def fractiles():
	with open('input.txt') as input_file:
	    testCases = input_file.readlines()
	numTestCases = testCases[0]
	testCases.remove(numTestCases)
	output_filename = 'output.txt'
	if os.path.exists(output_filename):
		os.remove(output_filename)
	for i in xrange(0, len(testCases)):
		testCase = testCases[i].split(' ')
		spotsToCheck = findSpotsToCheck(int(testCase[0]), int(testCase[1]), int(testCase[2]))

		
		
		with open(output_filename, 'a') as output_file:
			output_file.write('Case #' + str(i+1) + ': ' + str(spotsToCheck) + '\n')

fractiles()








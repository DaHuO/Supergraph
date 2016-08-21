def fractile(initialLength, complexity, students):
	studentPlacement = []
	studentSpacing = initialLength ** (complexity - 1) 
	for student in range(students):
		studentPlacement.append((student * studentSpacing) + 1)
	return studentPlacement 

def answer(caseNum, studentList):
	output = ""
	for student in studentList:
		output += str(student) + " "
	print("Case #" + str(caseNum) + ": " + output)
	
numCases = int(input())
for case in range(1, numCases + 1 ):
	line = input()
	listInput = line.split()
	k = int(listInput[0])
	c = int(listInput[1])
	s = int(listInput[2])
	answer(case, fractile(k, c, s))
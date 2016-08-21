
def main():

	import sys
	import string
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputEvacuationFile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + 2*test
		itemsNum = int(content[index])
		index += 1
		items = content[index].split()
		items = list(map(int, items))

		letters = list(string.ascii_uppercase)[0:len(items)]
		evacuation = findPlan(items,letters)
				## find full price
		
		outputStr = "Case #" + str(test+1) + ": "

		plan = " ".join(str(member) for member in evacuation)
		outputStr += plan
		outputStr += "\n"

		outputFile.write(outputStr)

def findPlan(items,letters):

	import heapq
	myDict = []
	answer = []

	if not items : return([])

	total = sum(items)
	for item in zip(items, letters):
		myDict.append([item[0],item[1]])

	while myDict:	
		myDict.sort()
		if total == 3 and len(myDict) == 3:
			answer.append(myDict[-1][1])
			myDict.pop()

		elif len(myDict) > 1:
			if 2*(myDict[-1][0] - 1) <= total - 2:
				answer.append(myDict[-1][1]+myDict[-2][1])
				myDict[-1][0] -= 1
				myDict[-2][0] -= 1

				if myDict[-2][0] == 0:
					myDict.pop(-2)
				if myDict[-1][0] == 0:
					myDict.pop()
			else:
				answer.append(myDict[-1][1]+myDict[-1][1])
				myDict[-1][0] -= 2
				if myDict[-1][0] == 0:
					myDict.pop()
			total -= 2
		else:
			answer.append(myDict[0][1])
			total -= 1
			myDict[0][0] -= 1
			if myDict[0][0] <= 0:
				myDict = []

	return(answer)

if __name__ == '__main__':
	main()

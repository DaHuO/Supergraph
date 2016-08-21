import operator

num_testcase = 0
partyNum = []
partyComposure = []

def sortNPick(partyMap, senNum):
	sorted_x = sorted(partyMap.items(), key=operator.itemgetter(1), reverse=True)
	result = ''
	if senNum == 3:
		partyMap[sorted_x[0][0]] = sorted_x[0][1] - 1
		result = result + sorted_x[0][0]
	elif senNum == 4:
		if sorted_x[0][1] == 2 and sorted_x[1][1] == 2:
			partyMap[sorted_x[0][0]] = sorted_x[0][1] - 1
			partyMap[sorted_x[1][0]] = sorted_x[1][1] - 1
			result = result + sorted_x[0][0] + sorted_x[1][0]
		else:
			partyMap[sorted_x[0][0]] = sorted_x[0][1] - 2
			result = result + sorted_x[0][0] + sorted_x[0][0]
	else:
		partyMap[sorted_x[0][0]] = sorted_x[0][1] - 1
		partyMap[sorted_x[1][0]] = sorted_x[1][1] - 1
		result = result + sorted_x[0][0] + sorted_x[1][0]
	
	return result
	
def process(totalNum, element):
	senNum = 0
	partyMap = dict()
	for i in range(totalNum):
		senNum = senNum + int(element[i])
		partyMap[chr(ord('A') + i)] = int(element[i])

	result = ''
	while senNum > 0:
		eva = sortNPick(partyMap, senNum)
		senNum = senNum - len(eva)
		result = result + eva + ' '
	return result
		
def main():
	f = open('A-small-attempt0.in', 'r')
	num_testcase = int(f.readline())
	while True:
		line = f.readline()
		if not line:
			break
		partyNum.append(int(line))
		
		line = f.readline()
		if not line:
			break
		partyComposure.append(line.split())
		
	f.close()
	
	f = open('output_small_text1.txt', 'w')
	for i in range(num_testcase):
		result = process(partyNum[i], partyComposure[i])
		f.write('Case #%d: %s\n' % ((i+1), result))
	
	f.close()
	
if __name__ == "__main__":
    main()
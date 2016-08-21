
num_testcase = 0
inputs = []

def process(input):
	#print 'input : ' + input
	if len(input) <= 0:
		return
		
	strList = []
	strList.append(input[0])
	
	for i in range(1, len(input)):
		c = input[i];
		
		tmpList = []
		for j in range(0, len(strList)):
		
			after = strList[j] + c
			tmpList.append(after)
			
			before = c + strList[j]
			tmpList.append(before)
			
		strList = tmpList
		
	strList.sort()
	result = strList[len(strList) - 1]
	#print 'result : ' + result
	return result

			
def main():
	f = open('A-small-attempt0.in', 'r')
	num_testcase = int(f.readline())
	while True:
		line = f.readline()
		if not line: break
		inputs.append(line)
	f.close()

	f = open('output_small_text1.txt', 'w')
	
	for i in range(0, len(inputs)):
		result = process(inputs[i])
		f.write('Case #%d: ' % (i+1) + result)
	f.close()
	
if __name__ == "__main__":
    main()
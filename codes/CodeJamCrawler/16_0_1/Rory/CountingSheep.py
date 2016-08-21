
def findMaxNumber(N):
	viewed = set(x for x in str(N))
	multiplier = 1
	while not _isViewedAll(viewed):
		if _isInfinityState(N*multiplier):
			return 'INSOMNIA'
		multiplier+=1
		viewed.update(x for x in str(N*multiplier))
	return N*multiplier

def _isInfinityState(number):
	if number == 0:
		return True
	return False

def _isViewedAll(viewed):
	if len(viewed) >= 10:
		return True
	return False

def createOutput(i,N):
  	return "Case #{}: {}".format(i, findMaxNumber(N))

def createOutputFile(inputFileName):
	inputFile = open(inputFileName,'r')
	outputFile = open('output.txt','w')
	T = int(inputFile.readline())
	for i in range(1,T+1):
		N = int(inputFile.readline())
		outputFile.write(createOutput(i,N)+"\n")

def main():
	T = int(input())
	for i in range(1, T+1):
  		N = int(input())
  		print(createOutput(i,N))

if __name__ == "__main__":
	main()
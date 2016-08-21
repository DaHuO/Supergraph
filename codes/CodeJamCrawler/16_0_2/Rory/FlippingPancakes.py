
def getMinFlips(S):
	S = _reduceInput(S)
	flips = S.count('-')*2
	if S[0] == '-':
		flips-=1
	return flips

def _reduceInput(S):
	A = [S[0]]
	for i in range(1,len(S)):
		if S[i] != S[i-1]:
			A.append(S[i])
	return A

def _createOutput(i,S):
  	return "Case #{}: {}".format(i, getMinFlips(S))

def createOutputFile(inputFileName):
	inputFile = open(inputFileName,'r')
	outputFile = open('output.txt','w')
	T = int(inputFile.readline())
	for i in range(1,T+1):
		S = inputFile.readline().strip()
		outputFile.write(_createOutput(i,S)+"\n")

def main():
	T = int(input())
	for i in range(1, T+1):
  		S = input()
  		print(_createOutput(i,S))


if __name__ == '__main__':
	main()

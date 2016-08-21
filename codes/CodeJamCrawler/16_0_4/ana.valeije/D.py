import sys
from math import sqrt
					
def solveCase(case, f, fout):
	K, C, S = f.readline().strip().split(' ')
	result = ''
	for i in xrange(1,int(K) + 1):
		result += str(i) + ' '
	writeLine(fout, case, str(result))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = sys.argv[1]
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()

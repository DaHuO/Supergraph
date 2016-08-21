import re;
import sys;
import io;
import math;
import fileinput

def func(argv):
	inputFile = argv[0];
	dolog_verbose(inputFile);
	
	with open(inputFile, 'r') as f:
		testCount = f.readline();
		answer = {}
		for i in range(int(testCount)):
			i+=1;
			dolog_verbose(i);
			answer[i] = solve_problems(f);

	outputFile = inputFile.replace('in','out')

	with open(outputFile, 'w') as f:
		dolog_verbose(answer);
		for k,v in answer.items():
			dolog_verbose('({0}) {1}'.format(k,v)); 
			f.write('Case #{0}: {1}\n'.format(k, v));

def solve_problems(f):
	numberOfSheep = f.readline().strip();
	dolog_verbose('Number of Sheep:' + numberOfSheep);
	
	if (testValid(numberOfSheep)):
		return determineCount(numberOfSheep);
	else:
		return 'INSOMNIA';
	
def testValid(n):
	n = int(n);
	if (n == 0 ):
		return False;
	return True;
	
def determineCount(n):
	n = int(n)
	numbers = list(range(10))
	count = 0;
	case = 0;
	while numbers:
		removed = [] 
		count+=1;
		case+=n;
		for i in numbers:
			dolog_verbose(str(i)+':'+str(case));
			if (str(i) in str(case)):
				removed.append(i);
				dolog_verbose(numbers);
		for i in removed:
			numbers.remove(i)
		dolog_verbose(case)
	return case
	
	
			
testing = False;
verbose = False;

# All below here be global configs;
# testing = True;
# verbose = True;

# All below here be util functions;
def dolog(string):
	if testing:
		print '[DOLOG]',
		print(string);
		
def dolog_verbose(string):
	if verbose:
		dolog(string);

def readInputFileAsArray(fileHandle):
	line = fileHandle.readline();
	if len(line) == 0:
		return False;
	return line.strip().split(' ');

def writeArrayAsOutputFile(fileHandle, array):
	dolog_verbose(array)
	fileHandle.write(' '.join(array));

if __name__ == "__main__":
	func(sys.argv[1:])
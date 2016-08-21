import re;
import sys;
import io;
import math;
import fileinput;

def func(argv):
	inputFile = argv[0];
	dolog_verbose(inputFile);
	
	populatePrimes()
	
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
			f.write('Case #{0}:\n'.format(k));
			for j,d in v.items():
				dolog_verbose('({0}) {1}'.format(j, ' '.join(d))); 
				f.write('{0} {1}\n'.format(j, ' '.join(d)));

def solve_problems(f):
	row = f.readline().strip();
	(length, resultCount) = row.split(' ')
	dolog_verbose('Length: {0}, Results: {1}'.format(length,resultCount))
	
	length = int(length)
	results = {}
	
	min = int('1' + '0'*(length-2) + '1', 2)
	max = int('1' + '1'*(length-2) + '1', 2)
	dolog_verbose('Min: {0}, Max: {1}'.format(min,max))
	current = min
	while len(results) < int(resultCount):
		testCase = "{0:b}".format(current)
		dolog_verbose(testCase)
		result = findDivisors(testCase)
		if result:
			results[testCase] = result
			dolog_verbose(len(results))
			dolog_verbose(result)
		current +=2
	return results
			
def findDivisors(testCase):	
	result = []
	for base in range(2,11):
		divisor = isPrime(int(testCase, base))
		if divisor is True:
			return False
		else:
			result.append(str(divisor))
	return result

primes = []

def populatePrimes():
	for i in range(3,1001,2):
		if isPrime(i) is True:
			primes.append(i)

def isPrime(n):
	sqrt = int(n**0.5)+1
	
	if n==2 or n==3: 
		return True
	if n%2==0 or n<2: 
		return 2
	
	
	for i in primes:
		if i > sqrt:
			break;
		if n%i==0:
			return i
	i = 999
	while i < sqrt:
		i+=2
		if n%i==0:
			return i

	return True
	
			
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
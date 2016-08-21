import pandas as pd
import re
from random import randint
import math

class prime(object):
    """docstring for test"""
    def __init__(self):
        super(prime, self).__init__()

    def getNumbers(self, n):
    	x = n-1
    	s = 0
    	while x % 2 == 0:
    		x = x/2
    		s = s+1
    	d = int(x)
    	return {'n': n, 'd': d, 's': s}

    def testPrime(self, a, **nums):
    	for i in range(0,nums['s']):
    		if pow(a,(pow(2,i) * nums['d']),nums['n']) in (1, nums['n']-1):
    			return 0
    			break
    	return 1
    def run(self, num):
        nums = self.getNumbers(num)
        #print (nums)
        if nums['n'] < 2047:
        	a = [2]
        elif nums['n'] < 1373653:
        	a = [2,3]
        elif nums['n'] < 25326001:
        	a = [2,3,5]
        elif nums['n'] < 2152302898747:
        	a = [2,3,5,7,11]
        elif nums['n'] < 3474749660383:
        	a = [2,3,5,7,11,13]
        elif nums['n'] < 341550071728321:
        	a = [2,3,5,7,11,13,17]
        elif nums['n'] < 3825123056546413051:
        	a = [2,3,5,7,11,13,17,19,23]
        else:
        	a = [2,3,5,7,11,13,17,19,23,29,31,37]

        result = 0

        for i in a:
        	result = self.testPrime(i, **nums) + result

        if result == 0:
        	return False
        else:
        	return True #N Primo

def is_prime(a):
    for i in range(2, int((a/2)-1)):
       if a%i == 0:
           return i
    return 0
def convert_base(a, b):
    a = str(a)
    aux = b
    for i in range(1, len(a)-1):
        b = b * aux
    result = 0
    for digit in a:
        result = result + int(digit) * b
        b = int(b / aux)
    return (result)
def create_valid_binary(nDigits):
    binary = "1"
    for i in range(1, nDigits-1):
        binary = binary+str(randint(0, 1))
    binary = binary + "1"
    return (binary)

inputCsv = pd.read_csv("input.txt", header=0)
nInputs = inputCsv.columns.values[0]
resultCases = []
p = prime()
for x in (inputCsv[nInputs].tolist()):
    nDigits = int(re.split("\\s+", x)[0])
    nValidBinarys = int(re.split("\\s+", x)[1])
    sucesso = 0
    result = []
    diferentBinarys = set()
    while(sucesso < nValidBinarys):
        testBinary = create_valid_binary(nDigits)
        while testBinary in diferentBinarys:
            testBinary = create_valid_binary(nDigits)
        diferentBinarys.add(testBinary)
        testBinary = str(testBinary)
        validate = True
        resultStr = str(testBinary)+"\t"
        for i in range(2,11):
            t = convert_base(testBinary, i)
            if p.run(t):
                t = is_prime(t)
                if (t) != 0:
                    if i == 10:
                        resultStr = resultStr +"\t"+ str(t)+"\n"
                        result.append(resultStr)
                        sucesso = sucesso + 1
                        # print(sucesso)
                    else:
                        resultStr = resultStr +"\t"+ str(t)
            else:
                break
    resultCases.append(result)
f = open('submission.txt','w')
for i in range(0, len(resultCases)):
    f.write("Case #"+str(i+1)+":\n")
    for j in resultCases[i]:
        f.write(j)
f.close() # you can omit in most cases as the destructor will call it

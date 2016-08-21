'''
Created on Mar 13, 2016

Codejam template

@author: Ozge
'''
from itertools import product
filepath = ''
fileprefix = 'C-small-attempt1' #Change

filepathname = filepath + fileprefix
infilename = filepathname + '.in'
outfilename = filepathname + '.out'
lines = open(infilename, 'rU').read().split("\n")
outfile = open(outfilename, 'w+')

tcases = int(lines[0]) #this never chaneges
linestart = 1 # this might change if there are parameters N, M, L etc
   
def converttoint(binary, base):
	decimal = 0
	for digit in binary:
		decimal = decimal*base + int(digit)
	return decimal

def isprime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
  
def generateBinary(N):
	binarylist=["".join(seq) for seq in itertools.product("01", repeat=N-2)]
	print(binarylist)
	newlist=[]
	for i in binarylist:
		newlist.append('1'+i+'1')
	return newlist 

def solve(N, J):
#	binarylist= generateBinary(N) #['100011','111111','111001']#

	counter=1
	result=[] #this is binary result
#	for i in binarylist:
	for binary in product((0, 1), repeat=N-2):
		binary = (1,) + binary + (1,)
		if counter>J: 
			break
		else:
			binaryelement=''.join([str(b) for b in binary])
			if solveinner(binaryelement):
				result.append(binaryelement)
				counter=counter+1
	return result
	 
def solveinner(listelement):
	isPrime=False
	for j in range(2, 11):
		if isPrime is False:
			number=converttoint(listelement, j)
			isPrime=isprime(number)
		else:
			return False #the binary is a prime
	if isPrime is False:
		return True # the number is not prime in any base

def createoutput(binarylist):
	dict={}
	for i in binarylist:
		dict[i]=finddivisors(i)
	return dict

def finddivisors(binarynumber):
	divisors=[]
	for j in range(2, 11):
		number=converttoint(binarynumber, j)
		#divs = [n for n in range(1,number+1) if number % n == 0]
		counter=0
		for n in range(1, number+1):
			if counter==1:
				break
			else:
				if number % n == 0 and n!=1 and n!=number:
					divisors.append(n)
					counter+=1
	return divisors

#print(createoutput(solve(16,50)))
#print(createoutput(solve(6, 3)))
for testcase in range(1, tcases+1): #change the value to the line number where the first case starts
	N, J = [int(x) for x in lines[testcase].split()]
	out = createoutput(solve(N,J)) #Assign solved value
#	casestr = 'Case #'+str(testcase)+': '+str(out)
	outstr= 'Case #'+str(testcase)+': '+'\n'
	for key, value in out.items():
		#print(key, " ".join(map(str, value)))  
		outstr=outstr+key+' '+" ".join(map(str, value))+'\n'
#	print (outstr)
	outfile.write(outstr+"\n")
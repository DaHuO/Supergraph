import string, math, random, time

numDig    = 32
numSol    = 500
solLim    = 10**5

def miller_rabin(n):
  if n == 1: return False

  d,r = n-1, 0
  while d %2 == 0:
    r+=1
    d/= 2 #We'll have n-1 = 2^r * d


  #if n >= 3825123056546413051: return -1 #too large of an input for us
  if n < 1373653: lstz = [2,3]
  elif n < 9080191: lstz = [31,73]
  elif n < 4759123141: lstz = [2,7,61]
  elif n < 2152302898747: lstz = [2,3,5,7,11]
  elif n < 3474749660383: lstz = [2,3,5,7,11,13]
  elif n < 341550071728321:  lstz = [2,3,5,7,11,13,17]
  elif n < 3825123056546413051: lstz = [2,3,5,7,11,13,17,19,23]
  else: lstz =[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]

  def try_composite(a):
    val = pow(a,d,n)
    if val == 1:
      return False
    for i in range(r):
      if val == n-1:
        return False
      val = pow(val,2,n)
    return True # n is definitely composite

  for a in lstz:
    if try_composite(a):
      return False

  return True

isPrime = mr = m_r = miller_rabin


def getAnyFactor(val):
  if val % 2 == 0:
    return 2
  for x in xrange(3,solLim, 2):
    if val % x == 0:
      return x
  return False

def convertToBase(array, base):
  number = 0
  for i in array:
    number = number * base + i
  return number

def convertToBase2Array(number):
  array = []
  while number > 0:
    array.append(number % 2)
    number /= 2
  return array[::-1]


def isJamcoin(number):
  numArray    = convertToBase2Array(number)
  answerArray = []

  if number % 2 == 0 or isPrime(number): # has to end with 1 for all numbers
    return False
  for base in xrange(2,11):
    baseNnumber = convertToBase(numArray, base)
    if isPrime(baseNnumber):
      return False

  for base in xrange(2,11):
    baseNnumber = convertToBase(numArray, base)
    factorVal = getAnyFactor(baseNnumber)
    if not factorVal :
      return False
    answerArray.append(factorVal)


  print convertToBase(numArray, 10), string.join([str(x) for x in answerArray], " ")
  return True

solutions = set()
print "Case #1:"
number = 2**(numDig -1) + 1
count = 0
while len(solutions) < numSol:
  count += 1
  number += 2
  if number not in solutions and isJamcoin(number):
    solutions.add(number)

print "Took", count, "iterations"

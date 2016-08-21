import copy
import math

def generateBounds(N):
  if N < 2:
    return [[''], ['']]
  start = ['1']
  end = ['1']
  while len(start) < N-1:
    start.append('0')
  start.append('1')
  while len(end) < N-1:
    end.append('1')
  end.append('1')
  return [start, end]

def binaryStringToBase(string, base):
  result = 0
  for ch in string:
    result *= base
    result += int(ch)
  return result

def binaryStringIncrement(string):
  for i in range(len(string) - 2, -1, -1):
    if string[i] == '0':
      string[i] = '1'
      break
    else:
      string[i] = '0'
  return string

# def findPrimes(N, maxBase):
#   primes = [[None] * (maxBase + 1)]
#   primes[1] = [2, 3]
#   start, end = generateBounds(N)
#   for base in range(2, maxBase + 1):
#     primes[base] = copy.deepcopy(primes[base-1])
#     upperLimit = int(math.sqrt(binaryStringToBase(end, base)) + 1)
#     for i in range (primes[base][-1] + 2, upperLimit + 1, 2):
#       isPrime = True
#       for prime in primes[base]:
#         if i % prime == 0:
#           isPrime = False
#           break
#       if isPrime:
#         primes[base].append(i)

def findPrimes(N):
  primes = [2, 3]
  for i in range (primes[-1] + 2, N, 2):
    isPrime = True
    for prime in primes:
      if i % prime == 0:
        isPrime = False
        break
    if isPrime:
      primes.append(i)
  return primes

def solve(N, J):
  primes = findPrimes(1000)
  start, end = generateBounds(N)
  current = copy.deepcopy(start)
  answers = []
  while current[0] == '1':
    if len(answers) == J:
      break
    temp = [binaryStringToBase(current, 10)]
    for i in range (2, 10 + 1):
      number = binaryStringToBase(current, i)
      for prime in primes:
        if number % prime == 0:
          temp.append(prime)
          break
    if len(temp) == 10:
      answers.append(temp)
    current = binaryStringIncrement(current)
  return answers

print("Case #1:")
answers = solve(32, 500)
for answer in answers:
  line = ""
  for number in answer:
    line += str(number) + " "
  print(line)

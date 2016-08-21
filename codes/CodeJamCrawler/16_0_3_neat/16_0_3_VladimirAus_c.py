filename = raw_input('Enter the filename: ')

#################
# Timing
import time
start = time.time()

# Opening file
defaultfn = 'c-init.in'
try:
  if len(filename) == 0:
    fi = open(defaultfn)
    filename = defaultfn
  else:
    fi = open(filename)
except:
  print "File cannot be opened", filename
  exit()

#################
# Solution.
# testCases = int(fi.readline())
results = []

def produceBase(str):
  result = list()
  for x in range(9):
    result.append(int(str, x+2))
  return result

def prepareNumbers(n, j):
  ln = n-2
  counter = 0
  case = 1
  casetime = time.time()
  while (int('1'*ln) >= counter):
    cntrBinStr = bin(counter)[2:]
    middle = '0'*(ln-len(cntrBinStr)) + cntrBinStr
    num = "1" + middle  + "1"
    bases = produceBase(num)
    print "Bases", bases
    basesPass = list()
    basesDivs = [int(num)]
    for base in bases:
      div = isPrimeOrDivisor(base)
      basesPass.append(div == -1)
      if (div == -1):
        break
      else:
        basesDivs.append(div)

    if sum(basesPass) == 0:
      print "Found match", case, "time:", str(time.time() - casetime), "sec"
      f = open('c-large.out','a')
      f.write(' '.join(map(str, basesDivs)) + '\n')
      f.close()

      if (j == case):
        break
      case += 1
      casetime = time.time()

    counter += 1

def isPrimeOrDivisor(num):
  optime = time.time()
  timemax = 5
  divisor = 2
  while (num % divisor > 0):
    if (time.time() - optime > timemax):
      print timemax, "sec timeout for", num
      return -1
    if (divisor*2 > num):
      return -1

    divisor += 1

  return divisor

# Uncomment for preparation.
# Small
n=16
j=50
# Large
n=32
j=500

# Read primes.
# f = open('primes.data')
# primes = list()
# for line in f:
#   primes.append(int(line.rstrip()))

f = open('c-large.out', 'w')
f.write("Case #1:" + '\n')
f.close()

prepareNumbers(n, j)

print "Total time:", str(time.time() - start), "sec"
exit()
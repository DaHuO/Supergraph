import sys

def isPrime(n, divisors, base):
  # if n == 2 or n == 3: 
  #   return True
  # if n < 2 or n%2 == 0:
  if n%2 == 0:
    # print("%d is divisible by 2" % n)
    # divisors.append(2)
    divisors[base] = 2
    return False

  if n%3 == 0:
    # print("%d is divisible by 3" % n)
    # divisors.append(3)
    divisors[base] = 3
    return False

  if n < 9:
    return True

  r = int(n**0.5) # +1?
  f = 5
  while f <= r:
    # print (f)
    if n%f == 0:
      # print("%d is divisible by %f" % (n, f))
      # divisors.append(f)
      divisors[base] = f
      return False

    if n%(f+2) == 0:
      # print("%d is divisible by %f" % (n, f+2))
      # divisors.append(f+2)
      divisors[base] = f+2
      return False

    f += 6
  return True  

def count(seed):
  # seed is a string

  # convert to binary and add 1
  nextNumber = int(seed, 2) + 1

  length = len(seed)
  strFormat = "{0:0%db}" % length
  res = strFormat.format(nextNumber)

  if (len(res) > length):
    return "OVERFLOW"
  return res

def count1(seed):
  nextNumber = int(seed, 2) + 2
  length = len(seed)
  strFormat = "{0:0%db}" % length
  res = strFormat.format(nextNumber)

  if (len(res) > length):
    return "OVERFLOW"
  return res



filename = sys.argv[1]

f = open(filename)
cases = int(f.readline().strip()) # this will be 1
jLength, jCount = [int(n) for n in f.readline().strip().split(' ')]

# middle = '0' * (jLength-2)
# print(middle)

seed = '1' + '0'*(jLength-2) + '1'
# for i in range (0, 20):
#   print(seed)   
#   seed = count1(seed)


print("Case #1:")

for c in range(0, jCount):
  # print("looking for sequence #%d" %(c+1))
  looking = True
  divisors = {}
  while looking:
    for base in range (2, 11):
      if base in divisors:
        continue

      if (seed.count('1')%2 == 0):
        divisors[3] = 2
        divisors[5] = 2
        divisors[7] = 2
        divisors[9] = 2

      totalValue = int(seed, base)

      if isPrime(totalValue, divisors, base):
        looking = True
        divisors.clear()

        # print("BREAKING")
        break
      else:
        looking = False
    if not looking:
      if(len(divisors) != 9):
        print('Everythig is very wrong!')

      print("%s %s" % (seed, ' '.join( [str(d) for d in divisors.values()]  )))

    seed = count1(seed)  


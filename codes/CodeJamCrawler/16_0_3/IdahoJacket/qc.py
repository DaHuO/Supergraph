import sys
from math import sqrt
def prime(n):
    if n < 2: return 1
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return x
    return 0


numCases = input()
for case in range( 1, numCases + 1 ):
  (n,j) = [int(x) for x in raw_input().split()]

  x = "1" + ("0" * ( n-2 ) ) + "1"

  nums = [int(x,b) for b in xrange(2,11)]

  output = "\n"
  found = 0
  while found < j:
    divisors = bin(nums[0])[2:]
    valid = True
    #print str(nums[0]) + " " + bin(nums[0])
    for i in nums:
      d = prime(i) 
      if d != 0:
        divisors += " " + str(d)
      else:
        valid = False
        break

    if valid:
      found += 1
      output += divisors
      if found < j:
        output += "\n"

    x = bin(nums[0] + 2)[2:]
    nums = [int(x,b) for b in xrange(2,11)]

  print 'Case #' + str( case ) + ': ' + str( output )

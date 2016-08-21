import math
def find_divisor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  print "Case #{}:".format(i)
  n, j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  cnt = 0
  maxiner = pow(2,n-2);
  for k in xrange(0,maxiner):
    if cnt == j:
      break
    tmp = "{0:b}".format(k)
    test = "1"+"0"*(n-2-len(tmp))+tmp+"1"
    #print test
    divisor = []
    for base in xrange(2,11):
      num = int(test,base)
      ret = find_divisor(num)
      if ret==0:
        break
      divisor.append(ret)

    if len(divisor) == 9:
      cnt = cnt+1
      print "{} {} {} {} {} {} {} {} {} {}".format(test, divisor[0], divisor[1],divisor[2],divisor[3],divisor[4],divisor[5],divisor[6],divisor[7],divisor[8])
  
  # check out .format's specification for more formatting options


#~ f_in = open('B-small-practice.in')
#~ f_out = open('B-small-practice.out', 'w')

#f_in = open('B-large-practice.in')
#f_out = open('B-large-practice.out', 'w')

## The number of test cases

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  #~ n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  n = int(raw_input())
  if (n == 0):
    print "Case #{}: INSOMNIA".format(i)
    continue
  found = [0]*10
  #~ print "Found is ", found
  currNum = n
  while (sum(found) < 10):
    for j in range(0,10):
      if str(j) in str(currNum):
        found[j] = 1
    currNum += n
  print "Case #{}: {}".format(i, currNum - n)
    
  # check out .format's specification for more formatting options


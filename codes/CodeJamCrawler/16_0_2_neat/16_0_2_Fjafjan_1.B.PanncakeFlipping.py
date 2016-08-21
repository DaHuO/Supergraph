#~ f_in = open('B-small-practice.in')
#~ f_out = open('B-small-practice.out', 'w')

#f_in = open('B-large-practice.in')
#f_out = open('B-large-practice.out', 'w')

## The number of test cases

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  #~ n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  pancakes = str(raw_input())
  flips = 0
  for j in range(1, len(pancakes)):
    if (pancakes[j] != pancakes[j-1]):
      flips += 1
  if pancakes[-1] == '-':
    flips += 1
  
  print "Case #{}: {}".format(i, flips)
    
  # check out .format's specification for more formatting options


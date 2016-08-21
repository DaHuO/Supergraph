def group_pancakes(string): #returns number of alternating groups
  last = ' '
  count = 0
  for s in string:
    if last != s:
      count = count+1 
    last = s
  return count

def flip_number(string):
  cakearray = list(string)
  reducedlist = group_pancakes(string)
  
#  print cakearray[len(cakearray)-1]
  if reducedlist % 2 == 1:
    if cakearray[len(cakearray)-1] == '+':
      reducedlist = reducedlist - 1
  elif reducedlist % 2 == 0:
    if cakearray[len(cakearray)-1] == '+':
      reducedlist = reducedlist - 1

  return reducedlist

t = int(raw_input())
for i in xrange(1,t+1):
  n = [str(s) for s in raw_input().split(" ")]
  print "Case #{}: {}".format(i,flip_number(n[0]))

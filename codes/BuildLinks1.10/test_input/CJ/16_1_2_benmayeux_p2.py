t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  lists = []
  missing = {} #keeps track of who has been accounted for
  for j in xrange(0, 2*n - 1):
    lists.append(raw_input())
  for list in lists: #find missing numbers
    for height in list.split(' '):
	  if missing.has_key(height):
	    missing[height] = not missing[height]
	  else:
	    missing[height] = True
  lostList = [] #compile and sort missing by height
  for j in missing:
    if missing[j]:
	  lostList.append(int(j))
  lostList.sort()  
  
  print "Case #{}: {}".format(i, ''.join(str(l) + ' ' for l in lostList))
"""TODO: Describe the contents of the module here. (shgao)
"""

from google3.pyglib import app
from google3.pyglib import flags


# flags.DEFINE_string('name', 'default', 'description')


FLAGS = flags.FLAGS
 

def find(lists):
  ml = []
#   print lists
  
  for c in xrange(0, len(lists[0])):
    count = {}
    for r in xrange(0, len(lists)):
#       print r, c
      ch = lists[r][c]
      if ch in count:
        count[ch] = count[ch] + 1
      else:
        count[ch] = 1
    for k,v in count.items():
      if v % 2 == 1:
#         print count
#         print k
        ml.append(k)
  
#   print ml
  ml2 = list(ml)
  for c in ml2:
    if ml.count(c) % 2 == 0:
      while c in ml:
        ml.remove(c)
    else:
      while ml.count(c) > 1:
        ml.remove(c)
        
  ml.sort()
#   print ml

  assert len(ml) == len(lists[0])
  return ml

  # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
n = int(raw_input())  # read a line with a single integer

for i in xrange(1, n + 1):  # test cases
  sz = int(raw_input())  # read a line with a single integer
  lists = []
  for r in xrange(0, 2*sz-1):  # list for each case
    l = [int(s) for s in raw_input().split(" ")]  # a list
    lists.append(l)
#   print lists
  ml = find(lists)
#   print ml
  assert len(ml) == len(lists[0])
  s = ''
  for c in ml:
    s = s + str(c) + ' '
  print "Case #{}: {}".format(i, s.strip())
    
    
# print "Case #{}: {}".format(i, l)
   



import sys

T = int(sys.stdin.readline())

for testcase in range(T):
  print "Case #{}:".format(testcase+1),
  nl = sys.stdin.readline().strip().split()
  k = int(nl[0])
  c = int(nl[1])
  s = int(nl[2])
  
  if s >= k // c:
    tile = 0
    while tile < k:
      num = 0
      for i in range(c):
        num *= k
        if tile < k:
          num += tile
        tile += 1
      print num+1,
      
    print
    
  else:
    print "IMPOSSIBLE"
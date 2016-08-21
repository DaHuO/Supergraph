from __future__ import print_function

T = int(raw_input())

for case in xrange(T):
  [K, C, S] = map(int, raw_input().split())
  
  print("Case #%d:" % (case + 1), end='')
  
  if C == 1:
    if S < K:
      print(" IMPOSSIBLE")
    else:
      for i in xrange(K):
        print(" %d" % (i + 1), end='')
      print()
  elif K == 1:
    print(" 1")
  else:
    kc = K ** (C - 1)
    x = 2
    y = 0
    ans = []
    
    while x + y <= K * kc and S > 0:
      if (x > K): print("FAIL")
      ans.append(x + y)
      x += 2
      y += kc + kc
      if (x > K and K % 2 == 1):
        x -= 1
      
      S -= 1
    
    if (x + y <= K * kc):
      print(" IMPOSSIBLE") # wrong
    else:
      for x in ans:
        print(" %d" % x, end='')
      print()
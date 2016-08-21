from itertools import combinations as cnk

import sys


tests = input ()
for test in range (tests):
  n, k = map (int, sys.stdin.readline().split())
  p = map (float, sys.stdin.readline().split())
  p = sorted(p)

  res = 0.0
  for i in range (k + 1):
    c = []
    for j in range (i):
      c.append (p[j])
    for j in range (n - k + i, n):
      c.append (p[j])
#    print (c)
    dp = [[0.0 for i in range(k+1)] for j in range (k+1)]
    dp[0][0] = 1.0
    for i in range (1, k+1):
      for j in range (1, k+1):
        dp[i][j] = dp[i-1][j-1] * c[i-1]  
      for j in range (k+1):
        dp[i][j] += dp[i-1][j] * (1 - c[i-1])
    res = max (res, dp[k][k/2])         
  print ("Case #" + str(test + 1) + ": " + str(res))

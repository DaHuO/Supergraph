import numpy as np

def hist(s):
  ret = np.zeros(26, dtype='int')
  for c in s:
    ret[ord(c)-ord('A')] += 1
  return ret

vals = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
mat = np.array(map(hist, vals))

def solve_case(st):
  h = hist(st)
  m = np.copy(mat)
  sol = np.zeros(10, dtype='int')
  for j in range(4):
    for i in range(26):
      if np.sum(m[:, i]) == 1:
        s = np.where(m[:, i] == 1)[0][0]
        cnt = h[i]
        sol[s] += cnt
        h -= cnt*m[s]
        m[s] = np.zeros(26)
        #print m[:, i], h[i]

  ret = ""
  for i in range(10):
    ret += str(i)*sol[i]
  return ret

#print solve_case(''.join(vals))
#exit(0)

T = int(raw_input())
for i in xrange(T):
  sol = solve_case(raw_input())
  print "Case #%d:" % (i+1), sol

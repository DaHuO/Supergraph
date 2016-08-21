

def solve(K, C, S):
  p = 1
  for c in range(C-1):
    p = p*K
  s = [1]
  for t in range(K-1):
    s.append(s[-1]+p)
    
  return ' '.join([str(x) for x in s])


f = open('D-small-attempt0.in')
fo = open('output_D_small.txt', 'w')

NT = int(f.readline())
for t in xrange(NT):
  S = f.readline().strip().split()
  K, C, S = int(S[0]), int(S[1]), int(S[2])
  fo.write('Case #' + str(t+1) + ': ' + str(solve(K, C, S)) + '\n')
  

f.close()
fo.close()
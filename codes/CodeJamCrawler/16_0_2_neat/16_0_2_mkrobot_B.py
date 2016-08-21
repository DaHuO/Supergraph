

def solve(S, c):
  if not S: return 0
  if S[0] == c: return solve(S[1:], c)
  o = '+'
  if c == '+': o = '-'
  return 1 + solve(S[1:], o)

f = open('B-large.in')
fo = open('output_B_large.out', 'w')

NT = int(f.readline())
for t in xrange(NT):
  S = f.readline().strip()[::-1]
  fo.write('Case #' + str(t+1) + ': ' + str(solve(S, '+')) + '\n')
  

f.close()
fo.close()
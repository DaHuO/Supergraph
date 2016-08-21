from sys import stdin

T = int(stdin.readline())

STD = {}
def ST(p, r, s):
  if (p, r, s) not in STD:
    STD[(p, r, s)] = STM(p, r, s)
  return STD[(p, r, s)]
    
def STM(p, r, s):
  if r == 0 and s == 0:
    return 'P'
  elif p == 0 and s == 0:
    return 'R'
  elif p == 0 and r == 0:
    return 'S'

  if p == r and p > s or s > p and s > r:
    return ST((p + 1) / 2, (r - 1) / 2, s / 2) + ST((p - 1) / 2, (r + 1) / 2, s / 2)
  if p > r and p > s or r > p and r == s:
    return ST(p / 2, (r + 1) / 2, (s - 1) / 2) + ST(p / 2, (r - 1) / 2, (s + 1) / 2)
  if p == s and p > r or r > p and r > s:
    return ST((p + 1) / 2, r / 2, (s - 1) / 2) + ST((p - 1) / 2, r / 2, (s + 1) / 2)

for t in range(T):
  N, R, P, S = [int(i) for i in stdin.readline().split()]
  if len(set([R, P, S, (R + P + S) / 3, (R + P + S) / 3 + 1])) != 2:
    print('Case #{}: IMPOSSIBLE'.format(t + 1))
  else:
    print('Case #{}: {}'.format(t + 1, ST(P, R, S)))

def solve(p):
  esc = []
  while sum(p) > 0:
    num, x = max((v, i) for i, v in enumerate(p))
    sen = chr(65+x)
    if num*2 > sum(p):
      sen += esc.pop()
    esc.append(sen)
    p[x] -= 1

  return ' '.join(esc)

t = int(input())
for c in range(1, t+1):
  input()
  p = list(map(int, input().strip().split(' ')))
  print('Case #%d: %s' % (c, solve(p)))

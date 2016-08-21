for tc in range(1, int(input())+1):
  N = int(input())
  s = {}
  for i in range(2*N-1):
    l = [int(x) for x in input().split()]
    for x in l:
      if x in s:
        s[x] += 1
      else:
        s[x] = 1
  res = []
  for x in s:
    if s[x]%2 == 1:
      res.append(x)
  res.sort()
  print('Case #{_tc}: {_sol}'.format(_tc=tc, _sol=' '.join([str(x) for x in res])))

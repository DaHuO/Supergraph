for tc in range(1, int(input())+1):
  K, C, S = [int(x) for x in input().split()]
  if C>K:
    C = K
  res = ''
  if S < K-C+1:
    res = 'IMPOSSIBLE'
  elif C==1:
    res = ' '.join([str(x) for x in range(1,K+1)])
  else:
    val = 0
    for i in range(1, C-2):
      val += i*(K**(C-i-1))
    val += (C-1)*K
    l = []
    for i in range(val-(K-C+1)+1, val+1):
      l.append(str(i))
    res = ' '.join(l)
  print('Case #{_tc}: {_sol}'.format(_tc=tc, _sol=res))

if __name__ == '__main__':
  TC = int(raw_input())
  for cc in range(1, TC + 1):
    K, C, S = [int(x) for x in raw_input().split()]
    power = [0] * C
    power[0] = 1
    for p in range(1, C):
      power[p] = power[p - 1] * K
    ans = []
    for p in range(K):
      x = 0
      for i in range(C):
        x += p * power[i]
      ans.append(str(x + 1))
    print 'Case #%d: %s' % (cc, ' '.join(ans))

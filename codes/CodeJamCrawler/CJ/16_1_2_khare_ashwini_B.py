from collections import defaultdict
T = int(raw_input())

for case in range(1, T+1):
  N = int(raw_input())
  d = defaultdict(int)
  for i in range(1, 2*N):
    in_list = [int(_) for _ in raw_input().split()]
    for el in in_list:
      d[el] += 1
  odd = []
  for k,v in d.items():
    if v % 2 == 1:
      odd.append(k)
  odd.sort()
  odd = [str(_) for _ in odd]
  ans = ' '.join(odd)
  print('Case #{}: {}'.format(case, ans))
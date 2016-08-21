from sys import stdin
from collections import Counter

T = int(stdin.readline())

for t in range(T):
  N = int(stdin.readline())
  c = Counter()
  for _ in range(2 * N - 1):
    c.update(int(i) for i in stdin.readline().split())
  missing = [i for (i,v) in c.most_common() if v % 2 == 1]
  missing.sort()
  print('Case #{}: {}'.format(t + 1, " ".join(str(i) for i in missing)))

  

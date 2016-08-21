#!/usr/bin/env python3

# preprocessing
sol = [{'P': 'P', 'R': 'R', 'S': 'S'}]
for i in range(12):
  sol.append({
    'P': ''.join(sorted((sol[-1]['P'], sol[-1]['R']))),
    'R': ''.join(sorted((sol[-1]['R'], sol[-1]['S']))),
    'S': ''.join(sorted((sol[-1]['S'], sol[-1]['P'])))
  })

T = int(input())
for case in range(1, T+1):
  N, R, P, S = map(int, input().split())
  rl = [t for t in sol[N].values() if t.count('P') == P and t.count('R') == R and t.count('S') == S]
  res = min(rl) if rl else 'IMPOSSIBLE'
  print("Case #{}: {}".format(case, res))


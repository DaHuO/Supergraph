from operator import mul
import fileinput

num_cases = int(raw_input())
for case in range(1,num_cases+1):
  num_friends = int(raw_input())
  friends = [0] + map(lambda x: int(x), raw_input().strip().split())
  chains = {}
  chain_len = 0
  best_cycle = 0
  for start in range(1,len(friends)):
    visited = {start: True}
    prev = -1
    cur = start
    while not(friends[cur] in visited):
      prev = cur
      cur = friends[cur]
      visited[cur] = True
    if friends[cur] == cur:
      pass
    elif friends[cur] == prev:
      pair = (prev, cur)
      if not(pair in chains):
        chains[pair] = len(visited)
      else:
        chains[pair] = max(len(visited), chains[pair])
    if friends[cur] == start:
      best_cycle = max(best_cycle, len(visited))
  best_chain = 0
  for pair in chains:
    (x,y) = pair
    if (y,x) in chains and x < y:
      best_chain += chains[pair]-2
    else:
      best_chain += chains[pair]
  answer = max(best_cycle, best_chain)
  print("Case #%d: %d" % (case, answer))

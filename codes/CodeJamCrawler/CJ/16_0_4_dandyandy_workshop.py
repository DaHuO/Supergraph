import math

T = int(raw_input())
for curcase in range(1, T+1):
  K, C, S = (int(x) for x in raw_input().split())
  print "Case #" + str(curcase) + ":",
  if S < math.ceil(K/C):
    print "IMPOSSIBLE"
    continue
  cursor = 0
  results = []
  while cursor < K:
    indices = [p if p < K else 0 for p in range(cursor, cursor+C)]
    cursor += C
    my_result = 0
    for x in range(len(indices)):
      my_result += indices[x] * (K ** x)
    results.append(my_result+1)
  print " ".join(str(x) for x in results)

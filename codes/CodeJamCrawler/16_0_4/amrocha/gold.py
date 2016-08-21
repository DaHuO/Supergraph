import math

def check_tiles(K, C, S):
  result = list()

  if (K == S):
    return [i for i in range(0, K)]

  free_checks = C - 2
  num_checks = max(1, int(math.ceil(float(K - free_checks)/2)))

  print 'NUM CHECKS: ' + str(num_checks)
  print 'S: ' + str(S)

  if num_checks > S:
    return ['IMPOSSIBLE']

  if C == 1:
    return [i for i in range(0, K)]

  free_skip = K * free_checks
  for i in range(2, free_checks+1):
    free_skip += K**i

  for i in range(0, num_checks):
    quadrant =  2*i
    quadrant_skip = quadrant * K

    tile = free_checks + 2*i + 1
    if tile >= K:
      tile = K-1

    result.append(free_skip + quadrant_skip + tile)

  return result


results = list()
with open('D-small-attempt3.in', 'r') as f:
  testcases = int(f.readline())
  for line in f:
    values = line.split(' ')
    k = int(values[0])
    c = int(values[1])
    s = int(values[2])
    print '(K: ' + str(k) +', C: ' + str(c) + ', S: ' + str(s) + ')'
    results.append(check_tiles(k, c, s))

print results

with open('result-D-small-3.txt', 'w') as f:
  for i, res in enumerate(results):
    f.write('Case #'+str(i+1)+': ')
    for tile in res:
      f.write(str(tile+1) + ' ')
    f.write('\n')

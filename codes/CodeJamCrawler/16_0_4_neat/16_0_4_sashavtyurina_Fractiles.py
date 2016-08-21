import sys

filename = sys.argv[1]

f = open(filename)
cases = int(f.readline())


for case in range(0, cases):
  K, C, S = [int(d) for d in f.readline().strip().split(' ')]

  # if K == 1:
  #   res = '1'
  # else:
  tiles = [str(d) for d in range(1, K+1)]
  res = ' '.join(tiles)

  if C == 1:  
    res = 'IMPOSSIBLE' if len(tiles) > S else res




  print('Case #%d: %s' % ((case+1), res))



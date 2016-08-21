import sys

def which_tiles(k, c, s):
  # print(k, c, s)
  if k != s:
    print('huh?')
    return []
  if s == 1:
    return [1]
  tiles = [1, k ** c]
  for j in range(s - 2):
    tiles.append(1 + (j + 1) * k ** (c - 1))
  return tiles


t = int(sys.stdin.readline())
for i in range(1, t + 1):
  k, c, s = [int(p) for p in sys.stdin.readline().strip().split()]
  print('Case #%d: %s' % (i, ' '.join([str(t) for t in which_tiles(k, c, s)])))

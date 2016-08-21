from sys import stdin
from collections import defaultdict

numbers = [
  'ZERO',
  'ONE',
  'TWO',
  'THREE',
  'FOUR',
  'FIVE',
  'SIX',
  'SEVEN',
  'EIGHT',
  'NINE'
]


singles = [
  {
    'G': 8,
    'U': 4,
    'W': 2,
    'X': 6,
    'Z': 0,
  },
  {
    'F': 5,
    'H': 3,
    'S': 7,
  },
  {
    'I': 9,
    'O': 1
  }
]
T = int(stdin.readline())

for tc in range(1, T+1):
  W = stdin.readline()
  letters = defaultdict(int)
  for l in W:
    letters[l] += 1
  result = []
  for current in singles:
    for l in current:
      x = letters[l]
      y = current[l]
      for _ in range(x):
        result.append(str(y))
      if x != 0:
        for a in numbers[y]:
          letters[a] -= x
  result = sorted(result)
  print "Case #%d: %s" % (tc, "".join(result))

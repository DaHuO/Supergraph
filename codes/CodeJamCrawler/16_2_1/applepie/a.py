import sys
from collections import defaultdict

lines = map(lambda l: l.strip(), sys.stdin.readlines())
N = int(lines[0])

def red(d, letter, num_str):
  if letter in d and d[letter] > 0:
    count = d[letter]
    for c in num_str:
      d[c] -= count
      if d[c] < 0:
        print "DAMN " + str(letter) + " " +  num_str
        print d
    return count
  else:
    return 0

for case in range(1, N+1):
  d = defaultdict(int)
  for c in lines[case]:
    d[c] += 1
  counts = [0] * 10
  counts[0] = red(d, 'Z', 'ZERO')
  counts[2] = red(d, 'W', 'TWO')
  counts[6] = red(d, 'X', 'SIX')
  counts[8] = red(d, 'G', 'EIGHT')
  counts[3] = red(d, 'H', 'THREE')
  counts[4] = red(d, 'R', 'FOUR')
  counts[5] = red(d, 'F', 'FIVE')
  counts[7] = red(d, 'V', 'SEVEN')
  counts[1] = red(d, 'O', 'ONE')
  counts[9] = red(d, 'I', 'NINE')
  if sum(d.values()) > 0:
    print "NO"

  answer = ""
  for i in range(10):
    answer += str(i) * counts[i]
    
  print "Case #{0}: {1}".format(case, answer)


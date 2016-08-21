file = "large.in"

def revenge_of_the_pancakes(S):
  S += '+'
  flips = 0
  last = S[0]
  for c in S:
    if c != last:
      flips += 1
      last = c
  return flips

with open(file) as handle:
  T = int(handle.readline())

  for x in range(T):
    S = handle.readline().strip()

    print "Case #{}: {}".format(x + 1, revenge_of_the_pancakes(S))

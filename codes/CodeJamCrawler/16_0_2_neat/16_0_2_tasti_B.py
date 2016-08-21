def flip(S, i):
  return list(reversed(map(lambda x: not x, S[:i]))) + S[i:]

def ignore_bottom(S):
  while len(S) > 0 and S[-1]:
    S.pop()

  return S

def number_to_flip(S):
  if S[0]:
    i = 0
    while i < len(S) and S[i]:
      i += 1

    return i
  else:
    return len(S)

def revenge_of_the_pancakes(S):
  count = 0
  S = ignore_bottom(S)
  while not all(S):
    S = flip(S, number_to_flip(S))

    count += 1
    S = ignore_bottom(S)

  return count

filename = 'B-large'
f = open(filename + '.in', 'r')
o = open(filename + '.out', 'w')

T = int(f.readline())

for t in range(T):
  S = map(lambda x: True if x == '+' else False, list(f.readline().replace('\n', '')))
  o.write('Case #%d: %d\n' % (t + 1, revenge_of_the_pancakes(S)))

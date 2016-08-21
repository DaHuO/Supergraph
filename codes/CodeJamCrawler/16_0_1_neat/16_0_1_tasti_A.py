def counting_sheep(N):
  if N == 0:
    return 'INSOMNIA';

  i = 0
  seen = set()
  while len(seen) < 10:
    i += 1
    seen = seen | set(list(str(N * i)))

  return str(N * i)

filename = 'A-large'
f = open(filename + '.in', 'r')
o = open(filename + '.out', 'w')

T = int(f.readline())

for t in range(T):
  N = int(f.readline())
  o.write('Case #%d: %s\n' % (t + 1, counting_sheep(N)))

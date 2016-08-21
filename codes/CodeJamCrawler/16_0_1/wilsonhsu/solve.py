def solve(N):
  numbers = set()
  digits = set()

  M = N

  while len(digits) < 10 and M not in numbers:
    numbers.add(M)
    digits.update([int(d) for d in str(M)])
    M += N

  if len(digits) == 10:
    return M-N
  else:
    return "INSOMNIA"


def run(name):
  f = open('{0}.in'.format(name), 'r')
  g = open('{0}.out'.format(name), 'w')
  T = int(f.readline())
  for t in range(T):
    N = int(f.readline())
    result = solve(N)
    g.write('Case #{0}: {1}\n'.format(t+1, result))
  f.close()
  g.close()

if __name__ == '__main__':
  run('A-large')

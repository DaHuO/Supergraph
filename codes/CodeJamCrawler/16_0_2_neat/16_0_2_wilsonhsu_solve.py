def flip(pancake):
  if pancake == '-':
    return '+'
  else:
    return '-'

def solve(pancakes):
  if '-' not in pancakes:
    return 0
  elif '+' not in pancakes:
    return 1
  else:
    k = pancakes.index(flip(pancakes[0]))
    return 1 + solve(pancakes[k:])

def run(name):
  f = open('{0}.in'.format(name), 'r')
  g = open('{0}.out'.format(name), 'w')

  T = int(f.readline())
  for t in range(T):
    pancakes = f.readline().strip()
    result = solve(pancakes)
    g.write('Case #{0}: {1}\n'.format(t+1, result))

  f.close()
  g.close()

if __name__ == '__main__':
  run('B-large')




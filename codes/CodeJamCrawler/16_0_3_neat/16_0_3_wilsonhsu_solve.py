import math

def find_factor(n):
  for k in range(2, round(math.sqrt(n)+1)):
    if n % k == 0:
      return k
  return 1

def value(digits, base):
  v = 0
  b = 1
  for i in range(len(digits)):
    if digits[-1-i] == 1:
      v += b
    b *= base
  return v

def jamcoin_factors(digits):
  '''Return list of factors if digits is a jamcoin.
     Otherwise return None.'''

  factors = []
  for base in range(2, 11):
    factor = find_factor(value(digits, base))
    if factor == 1:
      return None
    factors.append(factor)
  return factors

class Jamcoin:
  def __init__(self, digits, factors):
    self.digits = digits
    self.factors = factors
  def __repr__(self):
    return "{0} {1}".format(''.join([str(d) for d in self.digits]),
                            ' '.join([str(f) for f in self.factors]))

def find_jamcoins(digits, k, J, jamcoins):
  if len(jamcoins) == J:
     return

  if k == len(digits)-1:
    factors = jamcoin_factors(digits)
    if factors is not None:
      jamcoin = Jamcoin(digits, factors)
      jamcoins.append(jamcoin)
      print(len(jamcoins), jamcoin)
  else:
    digits0 = digits.copy()
    digits0[k] = 0
    find_jamcoins(digits0, k+1, J, jamcoins)
    digits1 = digits.copy()
    digits1[k] = 1
    find_jamcoins(digits1, k+1, J, jamcoins)
 

def solve(N, J):
  jamcoins = []
  digits = [1] + [0]*(N-2) + [1]
  find_jamcoins(digits, 1, J, jamcoins)
  return jamcoins

def run(name):
  f = open('{0}.in'.format(name), 'r')
  g = open('{0}.out'.format(name), 'w')

  T = int(f.readline())
  for t in range(T):
    fields = f.readline().split()
    N = int(fields[0])
    J = int(fields[1])
    jamcoins = solve(N, J)
    g.write('Case #{0}:\n'.format(t+1))
    for jamcoin in jamcoins:
      g.write('{0}\n'.format(jamcoin))

  f.close()
  g.close()

if __name__ == '__main__':
  run('C-small-attempt0')



import math
import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def liste_primes_erastothene(n):
    visited = [False for _ in range(n + 1)]
    visited[0] = visited[1] = True
    for i in range(2, n + 1):
        if visited[i]:
            continue
        for j in range(i*i, n + 1, i):
            visited[j] = True
    return [i for i in range(2, n + 1) if not visited[i]]

lp = liste_primes_erastothene(10000000)
llp = len(lp)

def get_divisor(p):
    r=math.sqrt(p)
    n = 0
    while n < llp and lp[n]<=r:
        if p%lp[n]==0:
            return lp[n]
        n+=1
    return False

def get_cases(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        N, J = [int(x) for x in f.readline().split()]
        return N, J

def find_jamcoin(N, J):
    b = '1' + ''.join(['0' for _ in range(N-2)]) + '1'
    d = int(b, 2)
    count = 0
    res = []
    while count < J:
        divisors = is_jamcoin(b)
        if divisors:
            count += 1
            res.append((b, divisors))
        d += 2
        b = int2base(d, 2)
    return res

def is_jamcoin(b):
    divisors = []
    for base in range(2,11):
        divisor = get_divisor(int(b, base))
        if not(divisor):
            return False
        else :
            divisors.append(divisor)
    return divisors

def b_print(res, T, filename):
    with open(filename, 'w') as f:
        line = "Case #1:"
        print(line)
        f.write(line + "\n")
        for t in range(T):
            line = "{0} {1}".format(res[t][0], ' '.join([str(x) for x in res[t][1]]))
            print(line)
            f.write(line + "\n")

if __name__ == '__main__':
    filename = 'testp3.txt'
    N, J = get_cases(filename)
    res = find_jamcoin(N, J)
    b_print(res, J, 'outputp3.txt')
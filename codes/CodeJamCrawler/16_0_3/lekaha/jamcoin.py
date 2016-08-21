import string, math
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

primes = [2]
def generate_primes(n):
    """ Acceess the data if only if nearby Reduce the cache miss """
    def cross_off(p, f):
        count = (len(f) - 1)/p
        j = count * p
        new_f = ''
        pp = []
        for k in xrange(count, p - 1, -1):
            if f[k] == '1' and j >= 0:
                pp.append(j)
            j -= p
        f = reduce(lambda x, y: x + '0' if y in pp or f[y] == '0' else x + '1', xrange(len(f)), '')
        return f
        
    def next_prime(p, f):
        n = p + 1
        while n < len(f) and f[n] == '0':
            n += 1
        return n

    flags = str(''.join(str(1) for i in xrange(n)))
    prime = 2
    global primes
    primes = [2]
    while prime <= n:
        flags = cross_off(prime, flags)
        prime = next_prime(prime, flags)
        primes.append(prime)
    # print primes
    print 'Amount of primes: ', len(primes)
    return len(primes)

# def is_prime(n):
#     for i in primes:
#         if n % i == 0:
#             return False
#         return True

def is_prime(n):
    if n < 2:
        return False
    
    x = int(math.sqrt(n))
    for i in xrange(2, x + 1):
        if n % i == 0:
            return False
    return True

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    m = n
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    primes = [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
    return m in primes

import random
def is_probable_prime(n, k = 2):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      # Use random.randint(2, n-2) for very large numbers
      for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in xrange(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

def is_probable_prime_2(n):
    if n % 2 or n%3 or n%5 or n%7 or n%11:
        return False
    return True

def find_next_polite_number(n, divisor):
    for i in xrange(2, int(n ** .5) , 1):
        p_number = n / i
        # if (n % i) == 0:
        if (n % i) == 0:
            if not i in divisor:
                divisor.append(i)
            return i
    return n

def gen_base_num(jam):
    return [int(int2base(int(jam, base), 10)) for base in xrange(2, 11, 1)]

def gen_jamcoin(length, find_count):
    l = length - 1
    s = 2 ** length
    jams = []
    # generate_primes(int(''.join(str(1) for i in xrange(length + 1))))
    # print primes
    for c in xrange((2 ** l) + 1, s, 1):
        jam = bin(c)[2:]
        if len(jams) < find_count and jam[len(jam) - 1] != '0':
            basesNum = gen_base_num(jam)
            print jam, basesNum
            divisor = []
            valid = True
            for i in xrange(len(basesNum)):
            #     if is_probable_prime(basesNum[i]):
            #         print basesNum[i]
            #         valid = False
            #         break
            #     else:
            #         basesNum[i] = find_next_polite_number(basesNum[i], divisor)
                num = find_next_polite_number(basesNum[i], divisor)
                if num == 1 or num == basesNum[i]:
                    valid = False
                    break
                else:
                    basesNum[i] = num
            if valid:
                jams.append((jam, basesNum))
    return jams

def load_input(filename = None):
    if not filename:
        return
    line_buffer = None
    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer

import sys  

def main(argv):
    if not argv:
        filename = __file__
        lines = ['1', '16 3']
    else:
        filename = argv[0]
        lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')
    print int(lines[0]) == (len(lines) - 1)
    for i in xrange(int(lines[0])):
        N, J = map(str, lines[i + 1].split(' '))
        jamcoins = gen_jamcoin(int(N), int(J))
        # jamcoins = None
        # print gen_base_num('1001')
        s =  'Case #%d:\n'%(i+1)
        if jamcoins:
            for j in xrange(len(jamcoins)):
                s += ('%s %s\n' % (jamcoins[j][0], ' '.join(str(jam) for jam in jamcoins[j][1])))
        f.writelines(s)
        print '%s'%s
    f.close()

if __name__ == '__main__':
    main(sys.argv[1:])
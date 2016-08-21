import sys

def get_digits(n):
  digits = set()
  while n > 0:
    digits.add(n%10)
    n /= 10
  return digits

def solve(n):
  if n == 0:
    return 'INSOMNIA'
  else:
    i = 0
    digits = set()
    while len(digits) < 10:
      i += 1
      digits |= get_digits(i * n)
    return i * n

def main():
  ntests = int(sys.stdin.readline())
  for ntest in xrange(ntests):
    n = int(sys.stdin.readline())
    print 'Case #{}: {}'.format(ntest + 1, solve(n))

if __name__ == '__main__':
  main()

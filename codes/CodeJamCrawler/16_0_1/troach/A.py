import sys

def main():
  t = int(sys.stdin.readline())
  for case in range(1, t+1):
    sys.stderr.write('processing case %d\n' % case)
    process_case(case)
  sys.stderr.write('Finished\n')

def process_case(case):
  n = int(sys.stdin.readline())
  digits = set(str(n))
  done = check_digits(digits)
  m = n
  insomnia = False
  while not done:
    m = m + n
    next_digits = set(str(m))
    if next_digits == digits:
      done = True
      insomnia = True
    else:
      digits = digits.union(next_digits)
      done = check_digits(digits)

  if insomnia is True:
    sys.stdout.write('Case #%d: INSOMNIA\n' % case)
  else:
    sys.stdout.write('Case #%d: %d\n' % (case, m))

def check_digits(digits):
  for i in range(10):
    if str(i) not in digits:
      return False
  return True

if __name__ == '__main__':
  main()
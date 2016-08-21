import sys


def read_one_line():
  return sys.stdin.readline().rstrip()


if __name__ == '__main__':
  num_cases = int(read_one_line())
  target_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

  for case in xrange(num_cases):
    result = 0
    seen_digits = set()
    i = 1
    N = int(read_one_line())
    num = i * N

    if N == 0:
      print 'Case #%d: %s' % (case + 1, 'INSOMNIA')
      continue

    while True:
      num = i * N

      for char in str(num):
        seen_digits.update([int(char)])

      if seen_digits.issuperset(target_set):
        break

      i += 1

    result = num

    print 'Case #%d: %s' % (case + 1, result)



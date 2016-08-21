
def read_int(): return int(raw_input())
def read_pair_list(): return [(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in raw_input().split()]
def read_int_list(): return [int(x) for x in raw_input().split()]
def read_pair(): return [int(x) for x in raw_input().strip().split(',')]
def read_string(): return raw_input().strip()


def parse_input():
  T = read_int()
  cases = []
  for _ in xrange(T):
    cases.append(read_string())
  return cases


def solve_case(word):
  res_left = [word[0]]
  res_right = []
  for letter in word[1:]:
    if ord(letter) >= ord(res_left[-1]):
      res_left.append(letter)
    else:
      res_right.append(letter)
  return ''.join(res_left[::-1]) + ''.join(res_right)

if __name__ == '__main__':
  for idx, args in enumerate(parse_input()):
    res = solve_case(args)
    print 'Case #%d:' % (idx + 1), res

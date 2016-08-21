import sys

def read_one_line():
  return sys.stdin.readline().rstrip()


HAPPY_SIDE = '+'
BLANK_SIDE = '-'


def flip(sequence):
  if BLANK_SIDE in sequence:
    sequence = sequence.replace(BLANK_SIDE, HAPPY_SIDE)
  else:
    sequence = sequence.replace(HAPPY_SIDE, BLANK_SIDE)

  return sequence[::-1]


def count_first_group(sequence):
  if len(sequence) == 1:
    return 1

  first_flip = sequence[0]
  count = 1

  for flip in sequence[1:]:
    if flip == first_flip:
      count += 1
    else:
      break

  return count


def solve(flip_sequence):
  num_flips = 0

  while True:
    count = count_first_group(flip_sequence)

    if count == len(flip_sequence) and HAPPY_SIDE in flip_sequence:
      return num_flips

    happy_side_count = flip_sequence.count(HAPPY_SIDE)
    blank_side_count = flip_sequence.count(BLANK_SIDE)

    # execute flip
    flip_sequence = flip(flip_sequence[0:count]) + flip_sequence[count:]
    num_flips += 1


if __name__ == '__main__':
  num_cases = int(read_one_line())

  for case in xrange(num_cases):
    flip_sequence = read_one_line()
    num_flips = solve(flip_sequence)

    print 'Case #%d: %s' % (case + 1, num_flips)




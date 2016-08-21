from itertools import chain
from collections import OrderedDict


DIGITS = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
DIGITS = {n: l.upper() for n, l in DIGITS.items()}
STEP1 = {'X': 6, 'Z': 0, 'U': 4, 'G': 8, 'W': 2}
STEP2 = {'H': 3, 'S': 7, 'O': 1, 'F': 5}

od = OrderedDict()
for key, number in chain(STEP1.items(), STEP2.items(), {'N': 9}.items()):
  od[key] = number


def main(text):
    result = []
    for key, number in od.items():
      while key in text:
        result.append(number)
        for l in DIGITS[number]:
          text = text.replace(l, '', 1)

    return sorted(result)


if __name__ == '__main__':
  from google import reader, writer
  input = reader()
  test_count = int(next(input))
  result = []
  for i in xrange(test_count):
    test = next(input)
    number = main(test)
    result.append('Case #%d: %s\n' % (i + 1, ''.join(map(str, number))))

  writer(result)

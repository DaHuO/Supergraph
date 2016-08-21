import string
import pprint
from collections import defaultdict, Counter

pp = pprint.PrettyPrinter(indent=4)

INPUT = "1-large"

f = open('%s.in' % INPUT, 'r')
o = open('%s.out' % INPUT, 'w')

T = int(f.readline().strip())

all_numbers = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
number_counters = defaultdict(Counter)

for idx, n in enumerate(all_numbers):
    number_counters[idx] = Counter(list(n))


def solve(incoming):

    def remove_all_by_letter(c, numbers, letter, id):
        while c[letter] > 0:
            numbers.append(id)
            c -= number_counters[id]
        return c, numbers

    c = Counter(list(incoming))
    pp.pprint(c)
    numbers = []

    c, numbers = remove_all_by_letter(c, numbers, 'Z', 0)
    c, numbers = remove_all_by_letter(c, numbers, 'G', 8)
    c, numbers = remove_all_by_letter(c, numbers, 'X', 6)
    c, numbers = remove_all_by_letter(c, numbers, 'S', 7)
    c, numbers = remove_all_by_letter(c, numbers, 'W', 2)
    c, numbers = remove_all_by_letter(c, numbers, 'U', 4)
    c, numbers = remove_all_by_letter(c, numbers, 'H', 3)
    c, numbers = remove_all_by_letter(c, numbers, 'O', 1)
    c, numbers = remove_all_by_letter(c, numbers, 'N', 9)
    c, numbers = remove_all_by_letter(c, numbers, 'F', 5)

    pp.pprint(c)

    return "".join([str(x) for x in sorted(numbers)])




for t in xrange(T):

    S = f.readline().strip()

    res = solve(S)
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)

f.close()
o.close()


print
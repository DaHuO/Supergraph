from collections import namedtuple, Counter

Test = namedtuple('Test', 'S')

DIGITS = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'.split()
DIGITS = {i: Counter(s) for i, s in enumerate(DIGITS)}

def read(line):
    return Test(line.strip())

def solve(test):
    letters = Counter(test.S)
    counts = Counter()

    for i, lt in enumerate('ZWUXG'):
        d = i * 2
        counts[d] = letters[lt]
        for t in range(counts[d]):
            letters -= DIGITS[d]

    for i, lt in enumerate('OHFS'):
        d = i * 2 + 1
        counts[d] = letters[lt]
        for t in range(counts[d]):
            letters -= DIGITS[d]

    counts[9] = letters['I']

    return ''.join(map(str, sorted(counts.elements())))

if __name__ == '__main__':
    infile = 'A-large.in'

    with open(infile) as src:
        lines = list(src.readlines())
    number = int(lines[0])
    tests = [read(line) for line in lines[1:]]

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))

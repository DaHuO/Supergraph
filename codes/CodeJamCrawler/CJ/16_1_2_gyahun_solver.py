from collections import namedtuple, Counter

Test = namedtuple('Test', 'lines')

def read(lines):
    return Test(tuple(tuple(map(int, line.split())) for line in lines))

def solve(test):
    #print(test.lines)
    counts = Counter(n for line in test.lines for n in line)
    return sorted(n for n in counts if counts[n] % 2)

if __name__ == '__main__':
    infile = 'B-large.in'
    from itertools import groupby

    with open(infile) as src:
        lines = list(src.readlines())
    number = int(lines[0])
    index = 1
    tests = []
    while index < len(lines):
        num = int(lines[index])
        tests.append(read(lines[index + 1: index + 2 * num]))
        index += 2 * num

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, ' '.join(map(str, solve(test)))))

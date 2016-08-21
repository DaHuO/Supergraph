import sys


def turnover(pancakes):
    return list(map(lambda x: '+' if x == '-' else '-', reversed(pancakes)))


lines = open(sys.argv[1]).readlines()[1:]
for i, line in enumerate(lines):
    pancakes = list(line.strip())
    count = 0
    while True:
        while pancakes and pancakes[-1] == '+':
            pancakes = pancakes[:-1]
        if not pancakes:
            print('Case #{}: {}'.format(i + 1, count))
            break
        if pancakes[0] == '-':
            count += 1
            pancakes = turnover(pancakes)
            continue
        j = 1
        while True:
            if pancakes[j] != '+':
                break
            j += 1
        count += 1
        pancakes[:j] = turnover(pancakes[:j])

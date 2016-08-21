import sys


lines = open(sys.argv[1]).readlines()[1:]
for i, line in enumerate(lines):
    line = line.strip()
    words = [line[0]]
    for w in line[1:]:
        words = [a + w for a in words] + [w + a for a in words]
    words.sort()
    print('Case #{}: {}'.format(i + 1, words[-1]))

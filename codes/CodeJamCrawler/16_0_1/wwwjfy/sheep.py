import sys


lines = open(sys.argv[1]).readlines()[1:]
for i, line in enumerate(lines):
    num = int(line.strip())
    if num == 0:
        print('Case #{}: INSOMNIA'.format(i + 1))
        continue
    num2 = num
    digits = set()
    while True:
        digits = digits.union(set(str(num2)))
        if len(digits) == 10:
            print('Case #{}: {}'.format(i + 1, num2))
            break
        num2 += num

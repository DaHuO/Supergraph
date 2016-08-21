import fileinput

f = fileinput.input()
T = int(f.readline())
for t in range(1, T+1):
    n = int(f.readline())
    if n == 0:
        print('Case #{0}: INSOMNIA'.format(t))
        continue
    digits = set()
    last = 0
    while len(digits) < 10:
        last += n
        for c in str(last):
            digits.add(c)
    print('Case #{0}: {1}'.format(t, last))

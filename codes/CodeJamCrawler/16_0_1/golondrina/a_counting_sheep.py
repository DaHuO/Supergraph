with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'
    seen_digits = [0] * 10
    mult = 1
    while True:
        next_n = mult * n
        for d in str(next_n):
            seen_digits[int(d)] = 1
        if all(seen_digits) == 1:
            return next_n
        mult += 1


f = open('out.txt', 'w')
for i in xrange(1, t + 1):
    n = int(lines[i])
    f.write('Case #%s: %s \n' % (i, count_sheep(n)))
f.close()

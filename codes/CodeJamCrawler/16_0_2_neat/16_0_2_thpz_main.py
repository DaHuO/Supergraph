fn = 'B-large'

in_f = file(fn + '.in', 'r')
out_f = file(fn + '.out', 'w')

t = int(in_f.readline())

for i in range(1, t + 1):
    s = in_f.readline().strip()

    c = 0
    while True:
        while s:
            if s.endswith('+'):
                s = s[:len(s) - 1]
            else:
                break
        if s:
            c += 1
            s = s.replace('-', 'x')
            s = s.replace('+', '-')
            s = s.replace('x', '+')
        else:
            break

    out_f.write('Case #{}: {}\n'.format(i, c))

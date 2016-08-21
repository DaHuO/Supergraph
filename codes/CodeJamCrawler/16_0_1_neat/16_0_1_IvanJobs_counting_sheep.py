in_file, out_file = 'A-large.in', 'A-large.out'

def ntimes(N, t):
    nl = map(int, list(str(N)))
    for i in range(len(nl)):
        nl[i] *= t

    shift = 0
    i = len(nl) -1
    while i >= 0:
        tmp = nl[i] + shift
        shift = tmp / 10
        nl[i] = tmp % 10
        i -= 1

    if shift == 0:
        return map(str, nl)
    else:
        h = [shift,]
        h.extend(nl)
        return map(str, h)


with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
    T = int(fin.readline().strip())
    for _t in xrange(1, T + 1):
        N = int(fin.readline().strip())

        if N == 0:
            fout.write('Case #%d: INSOMNIA\n' % (_t,))
        else:
            s = set(list(str(N)))
            times = 1

            while len(s) < 10:
                times += 1
                res = ntimes(N, times)
                for ch in res:
                    s.add(ch)

            fout.write('Case #%d: %s\n' % (_t, ''.join(res),))



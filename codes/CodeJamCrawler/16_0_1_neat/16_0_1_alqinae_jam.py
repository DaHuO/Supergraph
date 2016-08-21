with open('input.in', 'r') as file:
    with open('output.out', 'w') as out:
        T = int(file.readline().strip())
        for case in xrange(1, T + 1):
            N = int(file.readline().strip())
            if N == 0:
                out.write('Case #%d: INSOMNIA\n' % case)
            else:
                i = 0
                appeared = [False, False, False, False, False, False, False, False, False, False]
                while True:
                    i += 1
                    sheeps = i * N
                    sheepsStr = str(sheeps)
                    for digit in sheepsStr:
                        appeared[int(digit)] = True
                    if (all(a for a in appeared)):
                        out.write('Case #%d: %d\n' % (case, i * N))
                        break

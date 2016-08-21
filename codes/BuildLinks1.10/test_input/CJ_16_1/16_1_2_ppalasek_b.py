import itertools
import numpy as np

t = int(raw_input())

for tt in xrange(t):
    n = int(raw_input())

    combs = list(itertools.combinations(range(2 * n - 1), n))

    lines = []
    for i in xrange(2 * n - 1):
        line = map(int, raw_input().split())
        lines.append(line)

    for c in combs:
        guess = []

        res = set(range(2 * n - 1))
        missing = set(range(n))

        for i in c:
            guess.append(lines[i])

            res.remove(i)

        guess = sorted(guess)

        gn = np.asarray(guess)
        gt = gn.transpose()

        f = 0

        for j in res:
            found = False

            for k in xrange(n):
                same = True

                for l in xrange(n):
                    if (lines[j][l] != gt[k][l]):
                        same = False
                        break

                if (same):
                    f +=1 
                    missing.remove(k)
                    break

        if (f == n - 1):
            final = ' '.join(map(str, gt[list(missing)[0]]))

            break



    print 'Case #%d:' % (tt + 1),

    print final
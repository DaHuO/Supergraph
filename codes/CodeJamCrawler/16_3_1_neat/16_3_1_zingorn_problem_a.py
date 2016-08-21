import sys
from itertools import repeat

f = open(sys.argv[1], "r")
f_out = open("out.out", 'w')

print sys.argv[1]
n_tests = int(f.readline())


def problem_a(l):
    pol = [ int(x) for x in l.split(' ') ]
    pol_count = pol.__len__()
    ans = []

    while sum(pol) > 0:
        st = ''
        mx = max(pol)
        # print('max {0}'.format(mx))
        j = 0
        stop = 0

        while sum(pol) > 0 and stop != 2 and j < pol_count:
            if pol[j] == mx:
                pol[j] -= 1
                mx = max(pol)
                # print('new max {0}'.format(mx))

                stop += 1
                st += chr(65 + j)
                j = 0
            else:
                j += 1

        if mx > sum(pol) - mx:
            ff = ''
            j = 0
            while j < pol_count:
                if pol[j] != 0:
                    ff = chr(65 + j)
                    pol[j] -= 1
                    break
                j += 1
            ans.append(ff)

        if stop > 0:
            ans.append(st)

        if stop < 1:
            break
    return ' '.join(ans)

t = 1
while t <= n_tests:
    f.readline()
    line = f.readline()

    res = problem_a(line.rsplit("\n")[0])
    print res
    f_out.write("Case #" + str(t) + ": " + res + "\n")
    t += 1

